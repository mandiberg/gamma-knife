Gamma Knife is a simple process + scripts to run queries that are too big for the Wikimedia Petscan tool. This process is designed for dealing with queries that go very deep into category structures. These queries are too big so they timeout. 

Order of operations:

1. Run a petscan query for the depth that you want, returning only categories. Output it as a CSV. This is the query I used: https://petscan.wmflabs.org/?categories=People+by+ethnicity&depth=6&ns%5B14%5D=1&project=wikipedia

2. Put that CSV in this folder. Rename it search_terms.csv, replacing the file in the folder.

3. Run gamma_knife.py, which will take quite a while. It will query petscan for a 0 depth request for each category in the list. You can specify a Wikidata query: I only wanted to return pages about humans (Q5)

4. Run merge_csv.py, which will open up all the petscan CSV files, and merge them into one, removing all duplicates
