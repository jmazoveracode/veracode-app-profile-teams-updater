
# Veracode Application Profile Bulk Team Updater

This repository contains tools for interacting with the Veracode Application Profiles API to manage and update team assignments in bulk. The two main scripts are:

1. **fetch_applications.py**: Fetches application profiles and generates a CSV containing the application details.
2. **update_app_profiles_teams.py**: Updates the team GUID for the application profiles listed in a provided CSV file.

## Prerequisites

- Python 3.10.15
- Conda (preferred for environment management)
- Veracode API credentials configured using the `veracode-api-signing` plugin.

## Installation

### Using Conda (Preferred)

1. Clone the repository:
    ```bash
    git clone https://github.com/jmazoveracode/veracode-app-profile-teams-updater.git
    cd veracode-app-profile-teams-updater
    ```

2. Create and activate a Conda environment:
    ```bash
    conda create --name veracode-env python=3.10.15 -y
    conda activate veracode-env
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Using Virtualenv (Alternative)

1. Clone the repository:
    ```bash
    git clone https://github.com/jmazoveracode/veracode-app-profile-teams-updater.git
    cd veracode-app-profile-teams-updater
    ```

2. Create and activate a virtual environment:
    ```bash
    python3.10 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### General Workflow

1. **Run `fetch_applications.py` to generate `applications.csv`**:
    - Ensure your Veracode API credentials are configured correctly.
    - Execute the script to fetch application profiles:
        ```bash
        python fetch_applications.py
        ```
    - This will generate an `applications.csv` file containing application details.

2. **Prepare the CSV for team updates**:
    - Open the `applications.csv` file and review the entries.
    - Identify and store the `Team GUID` you wish to add to the application profiles.
    - Remove any applications you do not wish to update from the CSV.
    - Ensure the CSV only contains rows for applications that need updates.

3. **Run `update_app_profiles_teams.py`**:
    - Provide the input CSV file and the new `Team GUID` as arguments:
        ```bash
        python update_app_profiles_teams.py --input applications.csv --team_guid <NEW_TEAM_GUID>
        ```

### Example

To fetch applications and update their team GUID:

1. Fetch applications:
    ```bash
    python fetch_applications.py
    ```

2. Edit the generated `applications.csv` file to include only applications you want to update.

3. Update the applications:
    ```bash
    python update_app_profiles_teams.py --input applications.csv --team_guid 67a0dea8-cb2b-49d1-b7df-e5dbf52291cd
    ```

## File Structure

```
veracode-app-profile-teams-updater/
├── fetch_applications.py          # Script to fetch application profiles and generate CSV
├── update_app_profiles_teams.py   # Script to update team GUIDs in application profiles
├── requirements.txt               # Python dependencies
├── README.md                      # Documentation
```

## Notes

- Ensure your Veracode API credentials are configured in your environment for both scripts to function.
- Always review the generated `applications.csv` file before running `update_app_profiles_teams.py`.
- If the `update_app_profiles_teams.py` script encounters errors, the execution will stop, and a detailed error message will be displayed for debugging.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

If you encounter issues, please open an issue in the repository or contact the maintainers.
