import os
import csv

# Define the base path to the Results folder and the output file
base_path = '/groups/sbinlab/ruining/ATV/Results'
output_file = 'affinity.txt'

# Open the output file in write mode
with open(output_file, mode='w') as outfile:
    # Loop through each subdirectory in the Results folder
    for result_dir in os.listdir(base_path):
        result_path = os.path.join(base_path, result_dir)
        if os.path.isdir(result_path):  # Ensure it's a directory
            # Path to the 'output' folder inside each subdirectory
            output_folder = os.path.join(result_path, 'output')
            csv_file_path = os.path.join(output_folder, 'affinity_prediction.csv')

            if os.path.exists(csv_file_path):
                # Open and read the CSV file
                with open(csv_file_path, mode='r') as csv_file:
                    csv_reader = csv.DictReader(csv_file)

                    # Loop through the rows in the CSV file
                    for row in csv_reader:
                        affinity_value = row['affinity']  # Assuming the column is named 'affinity'

                        # Write the result_dir (Results subfolder name) and affinity value to the output file
                        outfile.write(f"{result_dir},{affinity_value}\n")

print(f"Affinity values have been saved to {output_file}.")
