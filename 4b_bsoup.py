# Run pip install requests beautifulsoup4 pandas before it
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
url = "https://quotes.toscrape.com/"  # This is a demo website with quotes

# Send a request to get the content of the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Website accessed successfully.")
    
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract quotes and authors (just an example)
    quotes = soup.find_all('span', class_='text')  # All quote texts
    authors = soup.find_all('small', class_='author')  # All author names

    # Store the extracted data in a list of dictionaries
    data = []
    for i in range(len(quotes)):
        quote = quotes[i].text
        author = authors[i].text
        data.append({"Quote": quote, "Author": author})

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv('scraped_quotes.csv', index=False)

    print("Data has been saved to 'scraped_quotes.csv'.")

else:
    print(f"Failed to retrieve the website. Status code: {response.status_code}")
