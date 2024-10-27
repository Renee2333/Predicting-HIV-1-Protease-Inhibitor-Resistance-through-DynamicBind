import pandas as pd

# Load the dataset (adjust the path if necessary)
df = pd.read_csv('C:/Users/Ruini/Desktop/project/data/mutation_2.txt', sep='\t')

# List of drug columns
drug_columns = ['FPV', 'ATV', 'IDV', 'LPV', 'NFV', 'SQV', 'TPV', 'DRV']

# Define output file paths (one for each drug)
output_files = {f"{drug}_value.txt": None for drug in drug_columns}

# Filter the data and save to respective output files
for drug in drug_columns:
    # Filter rows without NA in the current drug column
    filtered_data = df.dropna(subset=[drug])
    
    # Keep the 'CompMutList' column and drug column
    comp_mut_list = filtered_data[['CompMutList', drug]]
    
    # Define the file path for saving
    output_path = f"C:/Users/Ruini/Desktop/project/data/double mutation/{drug}_value.txt"
    
    # Save the filtered 'CompMutList' to a file
    comp_mut_list.to_csv(output_path, index=False, header=True)
    
    # Store the output path in the dictionary
    output_files[f"{drug}_value.txt"] = output_path