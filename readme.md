# Gamma Knife queries Wikipedia categories with Petscan

Gamma Knife is a simple process + scripts to run queries that are too big for the Wikimedia Petscan tool. This process is designed for dealing with queries that go very deep into category structures. These queries are too big so they timeout. 

## Order of operations:

1. Run a petscan query for the depth-1 that you want, returning only categories. Subtract 1 from the desire depth, because the gamma_knife.py query essentially adds one layer of depth. Output it as a CSV. This is the query I used: https://petscan.wmflabs.org/?categories=People+by+ethnicity&depth=5&ns%5B14%5D&project=wikipedia&format=csv

2. Put that CSV in this folder. Rename it search_terms.csv, replacing the file in the folder.

3. Run gamma_knife.py, which will take quite a while. It will query petscan for a 0 depth request for each category in the list. I think you can specify a Wikidata query: I only wanted to return pages about humans (Q5) but I couldn't get it to work, and figured out a workaround (see 5.).

4. Run merge_csv.py, which will open up all the petscan CSV files, and merge them into one, removing all duplicates

5. If you need to reconcile this list against a different list, you can use intersection_csv.py. I needed to reconcile my output against a list of all humans (e.g. Q5) which I had in a different list. For me, reconciling removed any categories, fictional characters, and non-biographical articles. 
