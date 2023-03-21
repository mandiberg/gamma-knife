import csv
import concurrent.futures
import requests
import shutil
import os
import re

# simple ChatGPT derived CSV downloader

# Define the URL to query
# these settings return only Articles about Humans
URL = "https://petscan.wmflabs.org/"
project = "wikipedia"
depth=0
wikidata = "Q5"
# ns is namespace. 
# %5B1%5D is [1] is articles
# ns="%5B1%5D"
# ns="[1]"
# Define the headers to send with each request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}


def search(query):
    print('gonna go searchin')
    # Build the query parameters

    # params = {
    #     "categories": query.replace(" ","+"),
    #     "format": "csv",
    #     "project":project,
    #     "depth":depth,
    #     "wikidata_prop_item_use":wikidata,
    #     # "ns":ns,
    #     "doit":""
    # }

    query_formated = query.replace(" ","+").replace("_","+")
    url_query = f"https://petscan.wmflabs.org/?categories={query_formated}&depth=0&ns%5B1%5D&project=wikipedia&format=csv&doit="
    print(url_query)
    # Send the request and get the response
    # response = requests.get(URL, params=params, headers=HEADERS)
    response = requests.get(url_query, headers=HEADERS)
    response.raise_for_status()

    # Parse the comma-separated values from the response
    values = response.text.strip().split(",")
    print("going to get: ",query)
    with open(f"output/{query}.csv", "wb") as file:
        file.write(response.content)


# Read the search terms from the CSV file
with open("search_terms.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    search_terms = [row[1] for row in reader]
    # # search_terms = [row[1] for row in reader if row[1] not in search_terms]
    # search_terms = []
    # [search_terms.append(x) for x in all_terms if x not in search_terms]
    # print(search_terms)

for term in search_terms:
    if not re.search("/", term) and not re.search("xpatriate", term) and not re.search("bassador", term):
    # term = term.replace("/","")
        try:
            move_file = os.path.join("output_6",term+'.csv')
            shutil.copy2(move_file, 'output') # target filename is /dst/dir/file.ext
            print('moved: ',move_file) 
        except:
            print("file failed:, ", move_file)
    else:
        print("bad term: ", term)

exit()
# Use concurrent.futures to run the search function for each term concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(search, term) for term in search_terms]
    concurrent.futures.wait(futures)
