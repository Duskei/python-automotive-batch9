import xml.etree.ElementTree as ET
import os

def get_medical_issues(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Missing local file at: {file_path}")

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        # Extract issues, strip whitespace, and ignore empty tags
        issues = [issue.text.strip() for issue in root.iter('Issue') if issue.text]
        return sorted(issues, key=lambda x: x.lower())
    except ET.ParseError as e:
        raise ET.ParseError(f"XML Syntax Error in {file_path}: {e}")