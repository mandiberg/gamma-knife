import csv

# Define the input and output file paths
INPUT_FILE = "search_terms.csv"
DIFFERENT_FILE = "level6.csv"
OUTPUT_FILE = "diff_rows.csv"

# Create a set to store unique rows
input_rows = set()
different_rows = set()
unique_rows = set()

# Open the input file and read its contents as a CSV
with open(INPUT_FILE, "r") as csvfile:
    reader = csv.reader(csvfile)

    # Loop over each row in the file
    for row in reader:
        # this gets rid of the UID from each query
        # row_without_first_column = row[1:]
        row[0] = 0

        # Convert the row to a tuple to make it hashable
        row_tuple = tuple(row)

        # Add the row tuple to the set of unique rows
        input_rows.add(row_tuple)

# Open the input file and read its contents as a CSV
with open(DIFFERENT_FILE, "r") as csvfile:
    reader = csv.reader(csvfile)

    # Loop over each row in the file
    for row in reader:
        # this gets rid of the UID from each query
        # row_without_first_column = row[1:]
        row[0] = 0

        # Convert the row to a tuple to make it hashable
        row_tuple = tuple(row)

        # Add the row tuple to the set of unique rows
        different_rows.add(row_tuple)

unique_rows = different_rows.difference(input_rows)

# Write the unique rows to the output file
with open(OUTPUT_FILE, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(unique_rows)