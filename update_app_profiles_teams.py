import sys
import requests
import csv
import json
import argparse
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC

# Base API URL
api_base = "https://api.veracode.com/appsec/v1"

# Headers
headers = {"User-Agent": "Python HMAC Example", "Content-Type": "application/json"}

def read_csv(file_path):
    """Reads the input CSV file and returns a list of dictionaries."""
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
            print(f"Read {len(data)} records from the CSV.")
            return data
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)

def fetch_application_details(app_guid):
    """Fetches the full application profile using the app GUID."""
    url = f"{api_base}/applications/{app_guid}"
    try:
        response = requests.get(url, auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
        print(f"Fetch response for application {app_guid}: {response.status_code}, Response: {response.text}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch details for application {app_guid}. Status code: {response.status_code}, Response: {response.text}")
            return None
    except requests.RequestException as e:
        print(f"Error fetching application details for {app_guid}: {e}")
        return None

def update_application_profile(app_guid, updated_payload):
    """Updates the application profile with the new payload."""
    url = f"{api_base}/applications/{app_guid}"
    try:
        response = requests.put(
            url,
            auth=RequestsAuthPluginVeracodeHMAC(),
            headers=headers,
            json=updated_payload
        )
        print(f"Update response for application {app_guid}: {response.status_code}, Response: {response.text}")
        if response.status_code == 200:
            print(f"Successfully updated application {app_guid}.")
        else:
            print(f"Failed to update application {app_guid}. Status code: {response.status_code}, Response: {response.text}")
            sys.exit(1)  # Stop the script on failure
    except requests.RequestException as e:
        print(f"Error updating application {app_guid}: {e}")
        sys.exit(1)  # Stop the script on exception

def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Update application profiles with new team GUIDs.")
    parser.add_argument("--input", required=True, help="Path to the input CSV file.")
    parser.add_argument("--team_guid", required=True, help="The new team GUID to update in application profiles.")
    args = parser.parse_args()

    # Read the CSV file
    data = read_csv(args.input)

    # Iterate over the records and update necessary application profiles
    for record in data:
        app_guid = record.get("App Profile GUID")
        current_team_guid = record.get("Team GUID")
        app_name = record.get("App Profile Name")
        new_team_guid = args.team_guid  # Use the team GUID passed as an argument

        if app_guid and current_team_guid == "N/A":
            print(f"Fetching details for application {app_name} ({app_guid}).")
            app_details = fetch_application_details(app_guid)
            if app_details:
                # Modify the retrieved payload with the new team GUID
                app_details["profile"]["teams"] = [{"guid": new_team_guid}]
                print(f"Updating application {app_name} ({app_guid}) with new Team GUID {new_team_guid}.")
                update_application_profile(app_guid, app_details)
        else:
            print(f"No update needed for application {app_name} ({app_guid}). Current Team GUID: {current_team_guid}")

if __name__ == "__main__":
    main()
