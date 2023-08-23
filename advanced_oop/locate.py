# Import the required modules
import csv
import requests
from bs4 import BeautifulSoup

# Define the input and output file names
input_file = "advanced_oop/trello_data.csv"
output_file = 'search_results.csv'

# Define the search engine URL (you can change it to Google if you prefer)
search_url = 'https://www.bing.com/search?q='

# Define the number of results to get for each query
num_results = 5

# Open the input file and read the data
with open(input_file, 'r') as input_csv:
    reader = csv.reader(input_csv)
    # Skip the header row
    next(reader)
    # Open the output file and write the data
    with open(output_file, 'w') as output_csv:
        writer = csv.writer(output_csv)
        # Write the header row
        writer.writerow(["Query","URLs"])
        # Loop through each row in the input file
        for row in reader:
            # Get the query from the first column
            query = row[0]
            # Encode the query for the URL
            encoded_query = requests.utils.quote(query)
            # Construct the full URL with the query
            full_url = search_url + encoded_query
            # Send a GET request to the search engine and get the response
            response = requests.get(full_url)
            
            # Parse the response content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
           
            # Find all the <a> tags with class=”b_algo” (these are the result links)
            headers = soup.find_all("a", class_="tilk")
            # Initialize an empty list to store the URLs
            
            headings = []
            # Loop through the links until we get enough URLs or run out of links
            for link in headers:
                # Get the href attribute of the link (this is the URL)
                result = link["href"]
                print(result)         
                # Append the URL to the list
                headings.append(result)
                # Break the loop if we have enough URLs
                if len(headings) == num_results:
                    break
            # Write the query and the URLs to the output file as a new row
            writer.writerow([query, headings])