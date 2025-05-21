import requests
from bs4 import BeautifulSoup
import csv

base_url = "http://quotes.toscrape.com/page/{}/"
page = 1
quotes_data = []

while True:
    response = requests.get(base_url.format(page))
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    if not quotes:
        break  # No more pages

    for quote in quotes:
        text = quote.find('span', class_='text').get_text(strip=True)
        author = quote.find('small', class_='author').get_text(strip=True)
        quotes_data.append([text, author])
    
    page += 1

# Save to CSV
with open('all_quotes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author'])
    writer.writerows(quotes_data)

print("All quotes scraped and saved to all_quotes.csv")
