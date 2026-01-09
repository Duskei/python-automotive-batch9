import pytest
import os
from med_logic import get_medical_issues

# Define your local path as a constant
LOCAL_FILE_PATH = r"D:\Wipro Training\python-automotive-batch9\med_data.xml"

@pytest.fixture
def local_xml_path():
    """Fixture to provide the local file path and verify it exists."""
    if not os.path.exists(LOCAL_FILE_PATH):
        pytest.fail(f"Test Setup Error: Local file not found at {LOCAL_FILE_PATH}")
    return LOCAL_FILE_PATH

def test_local_file_loading(local_xml_path):
    """Verifies that the local file can be loaded and is not empty."""
    result = get_medical_issues(local_xml_path)
    assert isinstance(result, list)
    # This ensures the XML actually contains data
    assert len(result) > 0, "The XML file exists but no 'Issue' tags were found."

def test_local_file_sorting(local_xml_path):
    """Verifies the returned list from your D: drive is sorted alphabetically."""
    result = get_medical_issues(local_xml_path)
    # Check if the list is equal to a sorted version of itself
    assert result == sorted(result, key=lambda x: x.lower())

def test_data_integrity(local_xml_path):
    """Verifies that items in the list are strings and not empty."""
    result = get_medical_issues(local_xml_path)
    for issue in result:
        assert isinstance(issue, str)
        assert len(issue) > 0