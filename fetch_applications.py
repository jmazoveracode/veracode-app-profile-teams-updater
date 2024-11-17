import sys
import requests
import json
import csv
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC

# Below is for Veracode US Commercial region. For logins in other regions uncomment one of the other lines
api_base = "https://api.veracode.com/appsec/v1"
# api_base = "https://api.veracode.eu/appsec/v1" # for logins in the Veracode European Region
# api_base = "https://api.veracode.us/appsec/v1" # for logins in the Veracode US Federal Region

headers = {"User-Agent": "Python HMAC Example"}

def fetch_applications(size=200):
    """Fetches a single page of application profiles."""
    try:
        url = f"{api_base}/applications/?page=0&size={size}"  # Request only page 0
        response = requests.get(url, auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
    except requests.RequestException as e:
        print("Error during API request:", e)
        sys.exit(1)

    if response.ok:
        data = response.json()
        apps = data["_embedded"]["applications"]
        print(f"Fetched {len(apps)} applications.")
        return apps
    else:
        print(f"Failed to fetch applications. HTTP status code: {response.status_code}")
        sys.exit(1)

def extract_app_info(app):
    """Extracts required information from a single app profile."""
    try:
        app_guid = app["guid"]
        app_name = app["profile"]["name"]
        # Check if 'teams' exists and is not empty
        if app["profile"].get("teams") and len(app["profile"]["teams"]) > 0:
            team = app["profile"]["teams"][0]  # Get the first team
            team_name = team["team_name"]
            team_guid = team["guid"]
        else:
            team_name = "N/A"
            team_guid = "N/A"
        return app_guid, app_name, team_name, team_guid
    except KeyError as e:
        print(f"Error extracting information: Missing key {e}")
        return None, None, None, None

def write_csv(apps, filename="applications.csv"):
    """Writes application data to a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(["App Profile GUID", "App Profile Name", "Team Name", "Team GUID"])
        for app in apps:
            app_info = extract_app_info(app)
            if app_info[0]:  # Only write rows with valid data
                writer.writerow(app_info)
    print(f"Application data has been written to {filename}")

if __name__ == "__main__":
    all_applications = fetch_applications(size=50)
    print(f"Total applications fetched: {len(all_applications)}")
    write_csv(all_applications)
