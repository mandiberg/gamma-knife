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
    # I think this wasn't working for me for some reason, but it should work...?
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

def move(search_terms):
    # Use this for loop if 
    for term in search_terms:
        # I am removing some of the categories from the new/moved files
        # if re.search(r'/wp-(?:admin|includes)/', response):
        # if not re.search("/", term) and not re.search("xpatriate", term) and not re.search("bassador", term):
        if not re.search('/|(Academic_staff_of_|Ambassadors|American_emigrants|Australian_emigrants|Canadian_emigrants|expatriates|Cultural_depictions|Fictional|Immigrants_to_|Lists_of_|Naturalised_citizens_|Novels_by_|People_by_|People_deported_|Refugees_in_|Works_|wikipedia_categories_|_from_|representatives_of_|delegates_of_|people_with_acquired_|buildings_and_structures_|biographical_museums_|american_mormon_|american_military_personnel_|academic_staff_of_|Academics_of_|Adaptations_of_|Battles_|Books_|Burial_sites_|Burials_|Christian_|Commonwealth_Games_|Compositions_by_|Cultural_depictions_of_|European_Games_competitors_|Films_about|Films_by_|Films_directed_by_|History_of_|James_Bond_|Marvel_Comics_|Olympic_|Paintings_|People_associated_with_|People_by_|People_educated_|Plays_|Recipients_of_|Sportspeople_by_|Staff_of_|Taxa_named_by_|Translators_of|Trotskyism_in_|United_States_|University_of_)', term):
            print(term)
            try:
                move_file = os.path.join("output_6",term+'.csv')
                shutil.copy2(move_file, 'output') # target filename is /dst/dir/file.ext
                print('moved: ',move_file) 
            except:
                print("file failed:, ", move_file)
        else:
            print("bad term: ", term)

    #this function will exit, and avoid the concurrent futures search process
    exit()



# Read the search terms from the CSV file
with open("search_terms.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    search_terms = [row[1] for row in reader]
    # # search_terms = [row[1] for row in reader if row[1] not in search_terms]
    # search_terms = []
    # [search_terms.append(x) for x in all_terms if x not in search_terms]
    # print(search_terms)

# Use this move function, if you have the full set downloaded, and want to avoid redownloading
# And you want to query against the full set, to produce a subset
# move(search_terms)


# Use concurrent.futures to run the search function for each term concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(search, term) for term in search_terms]
    concurrent.futures.wait(futures)
