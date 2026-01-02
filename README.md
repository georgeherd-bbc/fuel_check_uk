# fuel_check_uk
Scrapes current UK Government fuel price access data and outputs as an .xlsx Excel spreadsheet

Comes as Jupyter Notebook with markdown notation about the steps, and as a executable python script.

The python script and Jupyter Notebook files assume Python is installed. The script was built and tested using Python 3.10.5

**Required dependencies: BeautifulSoup4, Pandas, Requests, Openpyxl**

You can install these dependencies directly from your command line, using pip install in Python if not present - for example: 

```python3 -m pip install pandas``` 

Additionally, you can run the **run_script.py** file from the command line, which will automatically download any required dependencies, listed in the **requirements.txt file**.

The Guide to **running fuel_check_uk from CMD .md** file gives full instructions - including running the scripts in a virtual environment for additional safety.


### Fuel Data Notes and usage:
 
Only those operators that have signed-up to the road fuel monitoring scheme are included. In particular, it means data for some areas may not reflect the entire price picture - this appears to be especially true for Northern Ireland, where only Asda, Sainsbury's and Tesco are listed - with only 37 sites across the entire region.

More details on the fuel access data and the monitoring scheme can be found at the following UK Government website: [Access fuel price data](https://www.gov.uk/guidance/access-fuel-price-data)

It is anticipated the access fuel price data will cease to function some time in 2026, as the data becomes a mandatory reporting system for all UK forecourt operators from February 2026, as established by [The Motor Fuel Price (Open Data) Regulations 2025](https://www.legislation.gov.uk/ukdsi/2025/9780348275308)

VE3 Global has been appointed by the Department for Energy Security and Net Zero as the official 'aggregator' who will be making the data available to registered third-parties. Guidance on third-party registration, access and usage is awaited.
