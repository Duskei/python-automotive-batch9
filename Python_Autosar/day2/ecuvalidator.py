import xml.etree.ElementTree as ET
import os

# ===============================
# Step 0: Generate sample AUTOSAR XML if it doesn't exist
# ===============================
xml_file = "ECU_Config.arxml"

if not os.path.exists(xml_file):
    sample_xml = """<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR>
    <ECU-ID>EngineECU</ECU-ID>
    <CAN-BAUDRATE>500000</CAN-BAUDRATE>
    <OS>
        <TASK-PRIORITY>5</TASK-PRIORITY>
    </OS>
    <RTE-MAPPING>Rte_Engine</RTE-MAPPING>
</AUTOSAR>
"""
    with open(xml_file, "w") as f:
        f.write(sample_xml)
    print(f"Sample AUTOSAR XML file '{xml_file}' generated successfully!\n")

# ===============================
# Step 1: Load AUTOSAR XML file
# ===============================
try:
    tree = ET.parse(xml_file)
    root = tree.getroot()
except Exception as e:
    print("XML Parsing Failed:", e)
    exit()

# ===============================
# Step 2: Validate required parameters
# ===============================
report = {}

# ECU Name
ecu_name = root.find(".//ECU-ID")
report["ECU Name"] = "OK" if ecu_name is not None else "MISSING"

# CAN Baud Rate
can_baudrate = root.find(".//CAN-BAUDRATE")
report["CAN Baud Rate"] = "OK" if can_baudrate is not None else "MISSING"

# OS Task Priority
os_task_priority = root.find(".//TASK-PRIORITY")
report["OS Task Priority"] = "OK" if os_task_priority is not None else "MISSING"

# RTE Mapping
rte_mapping = root.find(".//RTE-MAPPING")
report["RTE Mapping"] = "OK" if rte_mapping is not None else "MISSING"

# ===============================
# Step 3: Generate validation report
# ===============================
print("===== ECU Configuration Validation Report =====")
for param, status in report.items():
    print(f"{param}: {status}")

overall = "FAILED" if "MISSING" in report.values() else "PASSED"
print(f"\nOverall Status: {overall}")