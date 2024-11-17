
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
- Ensure Python 3.10.15+ is installed.
- Install `virtualenv` (optional, but recommended):
  ```bash
  pip install virtualenv
  ```

### Veracode API Credentials
- Set up Veracode API credentials as environment variables. Refer to [Veracode Documentation](https://docs.veracode.com/r/c_api_credentials3#create-an-api-credentials-file-on-windows) for details.

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


## Alternative Setup Using Conda

If you prefer to use Conda for managing your environment, follow these instructions:

1. **Install Conda**: Make sure you have Conda installed. You can download it from [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

2. **Create a New Environment**: Create a new environment with Python 3.10.15:

   ```bash
   conda create --name veracode-env python=3.10.15
   ```

3. **Activate the Environment**:

   ```bash
   conda activate veracode-env
   ```

4. **Install Dependencies**: Use the `requirements.txt` file to install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. **Verify Installation**: Ensure all dependencies are installed correctly:

   ```bash
   python -m pip check
   ```

6. **Run the Scripts**: Once the environment is set up, you can run the provided scripts as described in the earlier sections.

Note: If you need to switch back to your base environment or another Conda environment, you can deactivate the current one:

```bash
conda deactivate
```

---

## License

This project is licensed under the MIT License.
