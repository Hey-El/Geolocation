import json
import os
import csv

def add_geolocation_to_json(json_path, latitude, longitude):
    """Step 1 Add geolocation data to a JSON file."""
    try:
        # Read the JSON data
        with open(json_path, 'r') as file:
            data = json.load(file)
            if 'geolocation' not in data:
                data['geolocation'] = {}
        
        # Add geolocation data
                data['geolocation']['latitude'] = latitude
                data['geolocation']['longitude'] = longitude
        
        # Save the modified JSON data
                with open(json_path, 'w') as file:
                    json.dump(data, file, indent=4)
          
                print(f"Geolocation ({latitude}, {longitude}) added to image: {json_path}")

    except Exception as e:
        print(f"Error adding geolocation to image {json_path}: {e}")

def process_directory(parent_directory_path, country_coordinates):
    """Process each image file in each subdirectory and add geolocation data based on folder name."""
    # Loop through each folder in the parent directory
    for root, dirs, files in os.walk(parent_directory_path):
        folder_name = os.path.basename(root)
        # Get the coordinates based on folder name
        coordinates = country_coordinates.get(folder_name, None)
        if coordinates:
                lat, lon = coordinates
                # Process each image file in the folder
                for filename in files:
                    file_path = os.path.join(root, filename)
                    # Check if the file is a JSON file
                    if file_path.lower().endswith('.json'):
                        add_geolocation_to_json(file_path, lat, lon)
                    else:
                        print(f"Skipping unsupported file type: {filename}")
        else:
            print(f"Coordinates not found for folder: {folder_name}")


if __name__ == "__main__":
    parent_directory_path = # Replace with your parent directory path
    country_coordinates = {
       #replace with your country coordinates
    }
    process_directory(parent_directory_path, country_coordinates)
       