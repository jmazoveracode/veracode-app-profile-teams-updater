
# Veracode Application Profile Bulk Team Updater

This project provides a Python-based utility to interact with the Veracode API for managing application profiles. 
The script fetches application profiles from a CSV file, verifies if a team GUID update is needed, and performs the update in bulk.

## Features

1. **Bulk Team GUID Update**:
   - Reads application profiles from a CSV file.
   - Verifies if the team GUID requires updating.
   - Updates only those profiles where a change is needed.

2. **Error Handling and Debugging**:
   - Displays API responses for debugging.
   - Stops execution upon critical errors while providing detailed feedback.

---

## Prerequisites

### Python Environment
- Ensure Python 3.8+ is installed.
- Install `virtualenv` (optional, but recommended):
  ```bash
  pip install virtualenv
  ```

### Veracode API Credentials
- Set up Veracode API credentials as environment variables. Refer to [Veracode Documentation](https://docs.veracode.com/) for details.

---

## Installation

### Clone the Repository
```bash
git clone <repository_url>
cd <repository_directory>
```

### Set Up Virtual Environment
```bash
python -m venv veracode-env
source veracode-env/bin/activate  # On Windows: veracode-env\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

### Script: Veracode Application Profile Bulk Team Updater

#### Description
Updates the team GUID of application profiles listed in a CSV file.

#### Command-Line Arguments
- `--input`: Path to the input CSV file containing app profile details.
- `--team_guid`: The new team GUID to assign.

#### Example
```bash
python update_app_profiles_teams.py --input applications_original.csv --team_guid 67a0dea8-cb2b-49d1-b7df-e5dbf52291cd
```

#### Workflow
1. **Input Validation**:
   - Ensures the provided CSV file is valid and readable.
2. **Profile Fetching**:
   - Verifies if the team GUID in the profile matches the one provided.
3. **Profile Update**:
   - Makes API requests to update the team GUID for applicable profiles.
4. **Error Reporting**:
   - Stops execution if critical errors are encountered.

#### Output
- Logs actions and API responses to the console.
- Provides clear feedback on whether updates succeeded or failed.

---

## File Structure

```
project/
│
├── update_app_profiles_teams.py # Script for bulk team GUID updates
├── requirements.txt            # Required dependencies
├── applications_original.csv   # Example input CSV file
└── README.md                   # Documentation
```

---

## Troubleshooting

### Common Issues
- **HTTP 400 Bad Request**: Ensure the provided GUIDs and payload data are valid.
- **Authentication Errors**: Confirm Veracode API credentials are correctly configured.

### Debugging
Use verbose logging to investigate API responses:
```bash
python update_app_profiles_teams.py --input <input_csv> --team_guid <new_team_guid> --verbose
```

---

## License

This project is licensed under the MIT License.

---
