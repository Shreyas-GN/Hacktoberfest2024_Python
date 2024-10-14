import requests  # Import the requests library to make HTTP requests
from bs4 import BeautifulSoup  # Import BeautifulSoup for parsing HTML

def scrape_titles(url):
    # Send a GET request to the specified URL
    response = requests.get(url)
    
    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all <h2> tags in the HTML (adjust the tag as necessary)
    titles = soup.find_all('h2')  
    
    # Loop through the found titles and print their text
    for title in titles:
        print(title.get_text())

# Prompt the user to enter the URL of the page to scrape
url = input("Enter the URL of the page to scrape: ")
# Call the function to scrape titles from the provided URL
scrape_titles(url)
