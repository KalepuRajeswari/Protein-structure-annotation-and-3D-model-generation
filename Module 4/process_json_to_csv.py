import json
import os
import csv

# Set the input and output path for JSON files
json_folder = 'C:/Users/INBIOSIS/Desktop/RPW_prot/colabfold_output_data'
output_csv = 'C:/Users/INBIOSIS/Desktop/RPW_prot/Json_output.csv'

# Check if the specified folder exists
if not os.path.exists(json_folder):
    print("The folder path you entered does not exist. Please check and try again.")
    exit()

try:
    with open(output_csv, 'w', newline='') as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile)
        # Write the header row
        writer.writerow(['Filename', 'Average pLDDT', 'pTM', 'Max PAE'])

        # Process each JSON file in the specified folder
        for filename in os.listdir(json_folder):
            if filename.endswith('.json') and 'scores' in filename:
                file_path = os.path.join(json_folder, filename)

                try:
                    # Load the JSON file
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                except Exception as e:
                    print(f"Error reading {filename}: {e}")
                    continue

                try:
                    # Extract data from JSON
                    if 'plddt' not in data or not isinstance(data['plddt'], list):
                        print(f"Invalid or missing 'plddt' in {filename}. Skipping.")
                        continue

                    average_plddt = sum(data['plddt']) / len(data['plddt'])
                    ptm = data.get('ptm', 'N/A')
                    max_pae = data.get('max_pae', 'N/A')

                    # Write the data to the CSV file
                    writer.writerow([filename, average_plddt, ptm, max_pae])
                except KeyError as e:
                    print(f"Missing key {e} in {filename}. Skipping.")
                except Exception as e:
                    print(f"Error processing {filename}: {e}. Skipping.")

    print(f"Data successfully written to {output_csv}")
except Exception as e:
    print(f"Error writing to CSV: {e}")
