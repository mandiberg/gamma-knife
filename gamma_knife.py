import csv
import concurrent.futures
import requests

# simple ChatGPT derived CSV downloader

# Define the URL to query
URL = "https://petscan.wmflabs.org/"
project = "wikipedia"
depth=0

wikidata = "Q5"



# Define the headers to send with each request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}


def search(query):
    # Build the query parameters
    params = {
        "categories": query.replace(" ","+"),
        "format": "csv",
        "project":project,
        "depth":depth,
        "wikidata_prop_item_use":wikidata,
        "doit":""
    }

    # Send the request and get the response
    response = requests.get(URL, params=params, headers=HEADERS)
    response.raise_for_status()

    # Parse the comma-separated values from the response
    values = response.text.strip().split(",")

    with open(f"output/{query}.csv", "wb") as file:
        file.write(response.content)


# Read the search terms from the CSV file
with open("search_terms.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    search_terms = [row[1] for row in reader]
    # # search_terms = [row[1] for row in reader if row[1] not in search_terms]
    # search_terms = []
    # [search_terms.append(x) for x in all_terms if x not in search_terms]
    # print(len(search_terms))

# Use concurrent.futures to run the search function for each term concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(search, term) for term in search_terms]
    concurrent.futures.wait(futures)
