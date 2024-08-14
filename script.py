import requests
from bs4 import BeautifulSoup
import pandas as pd

 
# URL of the webpage to scrape
url = "https://www.screener.in/company/RELIABLE/consolidated/"
 
# Send a GET request to the URL
response = requests.get(url)
 
# Check if the request was successful
if response.status_code == 200:
    print("Page retrieved successfully.")
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
    exit()
 
# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")
 
# Scrape the "Profit & Loss" data
profit_loss_table = soup.find("section", {"id": "profit-loss"}, class_="card card-large")
 
if profit_loss_table:
    datatable = profit_loss_table.find("table")
    
    table_data = []
    for row in datatable.find_all('tr'):
        row_data = [cell.text.strip() for cell in row.find_all(['th', 'td'])]
        table_data.append(row_data)
 
    # Convert the data into a DataFrame
    df = pd.DataFrame(table_data)
 
    # Display the DataFrame
    print(df)
 
    # Save the DataFrame to a CSV file
    df.to_csv("profit_loss.xlsx", index=False)
    print("Profit & Loss data saved to 'profit_loss.csv'.")
else:
    print("Profit & Loss table not found on the page.")
    exit()
 