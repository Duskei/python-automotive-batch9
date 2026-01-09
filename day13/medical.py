import xml.etree.ElementTree as ET
import os

def medical_issues(file_path):
    # Check if the path actually exists
    if not os.path.exists(file_path):
        return f"Error: The path '{file_path}' does not exist on this computer."

    try:
        # Load and parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot() # to know the where to start searching

        # Extract medical issues using iter() to catch tags anywhere in the file
        issues = [issue.text.strip() for issue in root.iter('Issue') if issue.text]

        # Sort alphabetically minding Case-insensitive sorting
        sorted_issues = sorted(issues, key=lambda x: x.lower())

        return sorted_issues

    except ET.ParseError:
        return "Error: Failed to parse XML. Check if the file format is valid."

#path to the XML file in the local system
local_path = r"D:\Wipro Training\python-automotive-batch9\med_data.xml"

# Execution
issues_list = medical_issues(local_path)

#checks if the returned value is a list before printing
if isinstance(issues_list, list):
    print(f"--- Alphabetical List of Medical Issues ({len(issues_list)} found) ---")
    for issue in issues_list:
        print(f"{issue}")
else:
    print(issues_list)