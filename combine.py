import os
import json

def gather_json_data(parent_directory_path, combined_json_path):
    """Step 2 Gathers JSON data from all subfolders and saves combined data to a single JSON file."""
    combined_data = []

    for root, dirs, files in os.walk(parent_directory_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            
            # Process only JSON files
            if file_path.lower().endswith('.json'):
                    try:
                        with open(file_path, 'r') as json_file:
                            json_data = json.load(json_file)
                            
                            # Append JSON data to the combined list
                            combined_data.append(json_data)
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")
    
    # Save combined data to a JSON file
    with open(combined_json_path, 'w') as outfile:
        json.dump(combined_data, outfile, indent=4)

# Example usage
parent_directory_path = #enter the directory path where the images are stored
combined_json_path = #enter the json file where the data will be exported to
gather_json_data(parent_directory_path, combined_json_path)