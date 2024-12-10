import csv
import os
import requests

# Set the directory where images will be saved
output_directory = "static/images"

# Make sure the directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Open the CSV file
with open('anime_data.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        image_url = row['image']
        image_id = row['id']
        
        # Download the image
        try:
            response = requests.get(image_url)
            response.raise_for_status()  # Check for request errors

            # Define the path to save the image (using .jpeg extension)
            image_path = os.path.join(output_directory, f"{image_id}.jpeg")

            # Write the image content to the file in JPEG format
            with open(image_path, 'wb') as img_file:
                img_file.write(response.content)
            
            print(f"Image {image_id} saved successfully.")
        
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {image_id}: {e}")

