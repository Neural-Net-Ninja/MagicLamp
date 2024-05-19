import re
from bs4 import BeautifulSoup


def extract_date(soup):
    # Find the element containing the date text
    date_text_element = soup.find(text=re.compile(r'\d{2}-\w{3}-\d{4}'))

    # Use a regular expression to extract the date from the text
    extracted_date = re.search(r'\d{2}-\w{3}-\d{4}', date_text_element).group()

    return extracted_date

# Use the function
# soup = BeautifulSoup(html_content, 'html.parser')
# print(extract_date(soup))