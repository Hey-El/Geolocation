import json
import csv

def extract_data_and_overwrite_csv(json_path, csv_path):
    # Step 3: Read the JSON file and extract data, grouping by geolocation to csv
    grouped_data = {}
    try:
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)
            
            for item in data:
                # Extract latitude and longitude from the geolocation field
                geolocation = item.get("geolocation", {})
                latitude = geolocation.get("latitude")
                longitude = geolocation.get("longitude")
                
                # Skip if latitude or longitude is missing
                if latitude is None or longitude is None:
                    continue
                
                # Extract the self_link if it exists
                permissions = item.get("permissions", [])
                if permissions and permissions[0].get("self_link"):
                    self_link = permissions[0]["self_link"]
                    # Extract the file ID from the self_link
                    file_id = self_link.split('/files/')[1].split('/')[0]
                    
                    # Generate the direct link format
                    direct_link = f"https://drive.google.com/uc?export=view&id={file_id}"
                    
                    # Use a tuple of latitude and longitude as the key for grouping
                    geo_key = (latitude, longitude)
                    
                    # Add the photo link to the corresponding geolocation group
                    if geo_key not in grouped_data:
                        grouped_data[geo_key] = {
                            "latitude": latitude,
                            "longitude": longitude,
                            "photo_links": [direct_link],
                            "description": ""  # Empty description field
                        }
                    else:
                        grouped_data[geo_key]["photo_links"].append(direct_link)
                        
    except Exception as e:
        print(f"Error reading {json_path}: {e}")
        return

    # Step 2: Write the grouped data to the CSV file
    headers = ["latitude", "longitude", "photo_links", "description"]
    try:
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=headers)
            
            # Write the headers to the CSV file
            csv_writer.writeheader()
            
            # Write the grouped data rows
            for geo_key, data in grouped_data.items():
                # Join photo links into a single string separated by commas
                data["photo_links"] = '\n'.join(data["photo_links"])
                csv_writer.writerow(data)

        print(f"CSV file {csv_path} has been successfully overwritten.")
    except Exception as e:
        print(f"Error writing to {csv_path}: {e}")

# Specify the paths
json_path =
csv_path = 

# Call the function
extract_data_and_overwrite_csv(json_path, csv_path)
