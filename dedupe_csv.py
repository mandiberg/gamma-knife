import csv

# Define the input and output file paths
INPUT_FILE = "combined.csv"
OUTPUT_FILE = "unique_rows.csv"

# Create a set to store unique rows
unique_rows = set()

# Open the input file and read its contents as a CSV
with open(INPUT_FILE, "r") as csvfile:
    reader = csv.reader(csvfile)

    # Loop over each row in the file
    for row in reader:
        # Skip the first column by slicing the row
        # this gets rid of the UID from each query
        row_without_first_column = row[1:]

        # Convert the row to a tuple to make it hashable
        row_tuple = tuple(row_without_first_column)

        # Add the row tuple to the set of unique rows
        unique_rows.add(row_tuple)

# Write the unique rows to the output file
with open(OUTPUT_FILE, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(unique_rows)