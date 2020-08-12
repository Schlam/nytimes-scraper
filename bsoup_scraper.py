import csv
import requests
from bs4 import BeautifulSoup



# Chosen filenames 
URL_FILE_NAME = "URLS.txt"
DATA_FILE_NAME = "DATA.csv"


def get_urls(fname = URL_FILE_NAME):
    """ Reads in all the urls from your url file """

    # Create empty list
    URLS = []

    # Open file containing urls
    with open(fname) as f:

        # Iterate over each line in the urls file
        for line in f.readlines():

            # Add to list
            URLS.append(str(line))
    
    return URLS


def get_data(URL):
    """ Gets the title and article body text from a url """

    # Get response from HTTP Request 
    response = requests.get(URL)
    
    # Parse response using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Get title of article
    title = soup.title.get_text()
    text = ""
    for line in soup.body.find_all('p'):
        
        # Add line to body of text
        text += line.get_text() 
        text += '\n'
    
    return (title,text)



if __name__ == "__main__":
    
    # Get the urls from file
    URLS = get_urls()

    # Get data from each url
    all_data = [get_data(url) for url in URLS]

    # Open file to write data into
    with open(DATA_FILE_NAME, 'w') as f:

        writer = csv.writer(f)

        # Iterate through data from each url
        for row in all_data:

            # Write to .csv file
            writer.writerow(row)
