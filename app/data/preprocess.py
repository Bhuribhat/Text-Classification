import csv

# Specify the input and output file paths
input_file = 'dataset.csv'
output_file = 'Text_Classification_Update.csv'

# Specify the row numbers to extract
rows_to_extract = set(range(1, 100_001)) | set(range(800_001, 900_001))

with open(input_file, 'r', newline='') as csvfile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(csvfile)
    writer = csv.writer(outfile)
    row_count = 0

    for row in reader:
        row_count += 1

        if row_count in rows_to_extract:
            writer.writerow(row)

        if row_count >= 900001:
            break