# Load the dataset
file_path = 'C:/Users/Ruini/Desktop/project/data/PI_DataSet.txt'

# Initialize lists to store filtered data
mutation_1 = []
mutation_2 = []
mutation_3 = []
mutation_4 = []
mutation_5 = []

# Uncertain mutation patterns (e.g., 'L63X', 'L90LM') that indicate quality issues
import re
uncertain_pattern = re.compile(r'[A-Z][0-9]+[A-Z]*X|[A-Z][0-9]+[A-Z]+[A-Z]+')

# Read and process the file
with open(file_path, 'r') as file:
    header = file.readline()  # Read the header
    for line in file:
        # Split the line into columns, focusing on the last one (mutation list)
        columns = line.strip().split('\t')
        mutations = columns[-1].split(', ')
        
        # Check if any mutation is uncertain (matches the uncertain pattern)
        if any(uncertain_pattern.search(mutation) for mutation in mutations):
            continue  # Skip this line if there's an uncertain mutation
        
        # Count the number of mutations and categorize based on that
        mutation_count = len(mutations)
        if mutation_count == 1:
            mutation_1.append(line)
        if mutation_count == 2:
            mutation_2.append(line)
        elif mutation_count == 3:
            mutation_3.append(line)
        elif mutation_count == 4:
            mutation_4.append(line)
        elif mutation_count == 5:
            mutation_5.append(line)

# Display the counts for each set
print(len(mutation_1),len(mutation_2), len(mutation_3), len(mutation_4), len(mutation_5))

# Define the file paths for saving the filtered sets
output_files = {
    "mutation_1.txt": mutation_1,
    "mutation_2.txt": mutation_2,
    "mutation_3.txt": mutation_3,
    "mutation_4.txt": mutation_4,
    "mutation_5.txt": mutation_5
}

# Save each filtered set into a separate file
output_paths = []
for filename, data in output_files.items():
    output_path = f"C:/Users/Ruini/Desktop/project/data/{filename}"
    with open(output_path, 'w') as outfile:
        outfile.write(header)  # Write the header
        outfile.writelines(data)  # Write the filtered data
    output_paths.append(output_path)


