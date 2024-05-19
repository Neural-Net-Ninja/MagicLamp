import pandas as pd
import requests
from bs4 import BeautifulSoup
from Today_date import todays_date
from exctract_date import extract_date


headers = {
    'User-Agent': 'Chrome/58.0.3029.110'
}

r = requests.get("https://www.5paisa.com/share-market-today/stocks-to-buy-or-sell-today", headers=headers)
r.content

# Use the 'html.parser' to parse the page
soup = BeautifulSoup(r.content, 'html.parser')

print(todays_date())
print(extract_date(soup))

if todays_date() == extract_date(soup):
    print("Today's date is: ", todays_date())
    print("Extracted date is: ", extract_date(soup))
    print("Data is up to date.")
    

# Then you can use the soup object to find elements on the page, for example:
# Find the table
table = soup.find('table', {'id': 'stock-table'})

# Find the header elements
headers = [header.text for header in table.find_all('th')]

# Find all the row elements
rows = table.find_all('tr')

data = {header: [] for header in headers}

# Loop through the rows
for row in rows[1:]:  # Skip the header row
    # Find all column elements
    cols = row.find_all('td')
    
    # Loop through the columns
    for header, col in zip(headers, cols):
        # Add the column data to the dictionary
        data[header].append(col.text.strip())

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
