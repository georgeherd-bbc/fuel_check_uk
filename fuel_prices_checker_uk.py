#!/usr/bin/env python
# coding: utf-8

# #### Building an Excel File which includes all the UK Government Access Fuel Price Data
# 
# 
# It using the dependencies: BeautifulSoup4, Pandas, Requests, Openpyxl**
# 
# If not already downloaded - install via terminal/cmd - or run github requirements.txt or run_script.py scripts - see README.MD in github for full directions
# 


#import the modules we need to build and export the DataFrame

from bs4 import BeautifulSoup #beautifulsoup 4 package to parse HTML
import requests 
import pandas as pd
import json
from datetime import datetime
import os  # this will allow us to specify which path we want to save the final output excel file to


# SCRAPE THE URLs:

# Define the URL of the webpage to scrape
url = 'https://www.gov.uk/guidance/access-fuel-price-data'

# use requests library to send GET request for the url

response = requests.get(url)

# Check if the request was successful - status should be 200 and parse with BeautifulSoup

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

# Initialize a list to store JSON URLs

json_url = []


# The URLs are all held within table markdown tags. To find all <td> elements in the table, using soup:

td_elements = soup.find_all('td')

# Iterate over each <td> element and extract the URLs ending with .json or .html (shell data)

for td in td_elements:
    url = td.text.strip()
    if url.startswith('https://') and url.endswith('.json') or url.endswith('.html'):
        json_url.append(url)



#building the dataframe

#headers - WITHOUT THIS - THE tesco_url ENTRY WILL REJECT THE REQUEST AND TIME OUT

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

#blank list to store the called json data

fuel_data = []

#loop through each URL and fetch the json data:

for url in json_url:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_data = response.json()
        fuel_data.append(json_data)
   # else:
    #    print(f"Failed to fetch data from {url}")
    
    
# Jet Fuel will return a Failed to fetch data response - this will be fixed below after creating a dataframe with the rest of the json data    
   
# Make DataFrame with pandas (pd) called df_fuel - and use the .json_normalize function get to record_path 'stations'

df_fuel = pd.json_normalize(fuel_data, record_path = 'stations')


# Fixing the missing Jet Local data

# Load json file from Jet URL:

url_jet = "https://jetlocal.co.uk/fuel_prices_data.json"  #The url for the jetlocal json data
headers = {"User-Agent": "Mozilla/5.0"}  # set a headers that will mimic a browser that works with this url

response = requests.get(url_jet, headers=headers)

if response.status_code == 200:
    json_data = response.json()
    df_jet = pd.DataFrame(json_data)
else:
    print(f"Request failed with status code {response.status_code}")


# place the json data in a dataframe - normalised to show the nested columns

df_jet = pd.json_normalize(json_data, record_path = 'stations')


# append the df-jet dataframe to our df_fuel dataframe

df_combinded_fuel = pd.concat([df_fuel, df_jet], ignore_index=True)


#rename df_combined back to df_fuel

df_combined = df_fuel


# Removing known PRL duplicates in the dataframe - due to MFG and PRL brand duplication


df_cleaned = df_fuel[~(df_fuel['postcode'].duplicated(keep=False) & df_fuel['address'].str.contains('PRL', case=False, na=False))]


# rename df_fuel_clean to df_fuel_uk 

df_fuel_uk = df_cleaned


# Add correctly formatted Latitude and Longitdue formats - replacing string objects with float numbers

#rename lat and longitude columns to single words

df_fuel_lat = df_fuel_uk.rename(columns={'location.latitude' : 'latitude', 'location.longitude' : 'longitude'})

#convert lat and long from string object to float numbers

df_fuel_lat['latitude'] = df_fuel_lat.latitude.astype(float)
df_fuel_lat['longitude'] = df_fuel_lat.longitude.astype(float)

# rename all that back to df_fuel_uk - using a copy of the dataframe to avoid potential slice/filter issues

df_fuel_uk = df_fuel_lat.copy()

# Exporting the final DataFrame to an Excel file format - in this case stored on a hard-drive volume

# use datetime to append date to file name

current_date = datetime.now().strftime('%d-%m-%Y')    #will date stamp the output file

output = f'fuel_prices_uk_{current_date}.xlsx'  #name of output file + date stamp

# Specify the path to save the file 

path_to_save = input("Please type the path location to save your file, for example C:\Data or /Volumes/portable_drive/data (DO NOT ADD FILENAME:    ")

path_to_save_expanded = os.path.expanduser(path_to_save)

# Full file path

file_path = os.path.join(path_to_save_expanded, output)

#convert fuel DataFrame data to Excel format and store in directory specified above with date appended

df_fuel_uk.to_excel(file_path, index = False)

