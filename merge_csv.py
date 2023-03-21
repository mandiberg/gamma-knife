import os
import csv

# simple ChatGPT derived CSV merger

# Define the input and output folder paths
INPUT_FOLDER = "output"
OUTPUT_FILE = "final_list_unique.csv"

# Create a set to store unique rows
unique_rows = set()

counter =0

# Loop over each file in the input folder
for filename in os.listdir(INPUT_FOLDER):
    # Skip any non-CSV files
    if not filename.endswith(".csv"):
        continue
    print(counter)
    # Open the file and read its contents as a CSV
    with open(os.path.join(INPUT_FOLDER, filename), "r") as csvfile:
        reader = csv.reader(csvfile)

        # Loop over each row in the file
        for row in reader:
            row[0] = 0
            # print(row)
            # title = row[1]
            # pageid = row[2]
            # print(pageid)
            # # print(row[2])
            # # Convert the row to a tuple to make it hashable
            # row_tuple = (title, pageid)
            row_tuple = tuple(row)

            # Add the row tuple to the set of unique rows
            unique_rows.add(row_tuple)
    counter += 1

# Write the unique rows to the output file
print('going to attempt to save file')
with open(OUTPUT_FILE, "w", newline="") as csvfile:
    print('have fileout open: ',OUTPUT_FILE)
    writer = csv.writer(csvfile)
    writer.writerows(unique_rows)
    print('written!')
