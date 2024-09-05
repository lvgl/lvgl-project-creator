#!/usr/bin/env python3

import json
import requests

# Function to fetch JSON content from a URL
def fetch_json(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

# List to hold all the JSON content
all_json_data = []

# Read the file containing URLs to JSON files
with open('manifests', 'r') as file:
    urls = file.readlines()

# Fetch and concatenate JSON data from each URL
for url in urls:
    url = url.strip()  # Remove any extra whitespace or newlines
    if url:  # Ensure the URL is not empty
        print(f"Fetching {url}")
        json_data = fetch_json(url)
        all_json_data.append(json_data)

# Save the concatenated JSON data to a new file
with open('manifest_all.json', 'w') as outfile:
    json.dump(all_json_data, outfile, indent=4)

print("All JSON data has been concatenated and saved to 'manifest_all.json'.")

