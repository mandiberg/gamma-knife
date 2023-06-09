# Gamma Knife queries Wikipedia categories with Petscan

Gamma Knife is a simple process + scripts to run queries that are too big for the Wikimedia Petscan tool (https://petscan.wmflabs.org/). This process is designed for dealing with queries that go very deep into category structures. These queries are too big so they timeout. 

## Order of operations:

1. Run a petscan query for the depth-1 that you want, returning only categories. Subtract 1 from the desire depth, because the gamma_knife.py query essentially adds one layer of depth. Output it as a CSV. This is the query I used: https://petscan.wmflabs.org/?categories=People+by+ethnicity&depth=5&ns%5B14%5D&project=wikipedia&format=csv

2. Put that CSV in this folder. Rename it search_terms.csv, replacing the file in the folder.

3. Run gamma_knife.py, which will take quite a while. It will query petscan for a 0 depth request for each category in the list. I think you can specify a Wikidata query: I only wanted to return pages about humans (Q5) but I couldn't get it to work, and figured out a workaround (see 5.).

4. Run merge_csv.py, which will open up all the petscan CSV files, and merge them into one, removing all duplicates

5. If you need to reconcile this list against a different list, you can use intersection_csv.py. I needed to reconcile my output against a list of all humans (e.g. Q5) which I had in a different list. For me, reconciling removed any categories, fictional characters, and non-biographical articles. 

## Cool, but why call it Gamma Knife?

The Petscan tool used to be called Catscan. Catscan was obviously a play on a portmanteau of Category Scan, and the medical CT scan, which is pronounced "cat scan". Apparently the upgraded version of Catscan was called Petscan, again a play on the PET scan which is a kind of "upgraded" CT scan (https://en.wikipedia.org/wiki/Positron_emission_tomography). The PET scan is used in cancer detection, which why I had one. And using this tool with the same/similar name for all these years has been a little bit triggering. 

A Gamma Knife (https://en.wikipedia.org/wiki/Gamma_Knife) is a high precision radio surgical tool used in brain surgery. The Gamma Knife was in the basement of the cancer wing of the hospital, and while I did not have to have it used on me, I walked past the sign each time I went there. The metaphor breaks down a bit, as it isn't a scanner, and the Gamma Knife excises by destroying, not physically removing, but I think my thought was that this was a very focused form of intervention. And more so, it seemed like a way of exorcising the bad vibes from the petscan name. 

## OK... but why did you need this in the first place?

I needed to re-run some petscan queries that I ran in 2021. The 2021 queries are in a forthcoming article to be published in *Social Text*. I needed to rerun these for a related article that will be published in *The Atlantic*. The People by Ethnicity data folder contains the working data for an article in The Atlantic. For this data, I used Gamma Knife to query the People by Ethnicity category to a total depth of 6 (e.g. petscan to depth of 5, and then Gamma Knife with depth 0), and excluded a set of categories listed in categories_to_exclude.txt. The list of all excluded categories is in list_of_excluded_categories.txt, with an explanation of the rationale. I reconciled the Gamma Knife output against a list of all 1.9M en wiki articles (generated via a Wikidata dump, using this process: https://github.com/mandiberg/topic-model-wikipedia). The final list of articles included in the full set of People by Ethnicity in final_list_unique_intersect_wikidata_d5_v2_rmXYZ_809492.csv and the list of all articles in the People of African Descent is in final_list_unique_intersect_wikidata_People_African_descent_59066.csv. The corresponding Wikidata is in Wikidata_Count_P172_with_enwiki_page_03242023.csv. 