import xml.etree.ElementTree as ET
import os
from xml.dom import minidom

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.txt")
OUTPUT_FILE = os.path.join(BASE_DIR, "cars.xml")

def create_xml_from_txt():
    cars = {}

    with open(DATA_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            key, value = line.split(":", 1)
            car_id, field = key.split(".", 1)

            if car_id not in cars:
                cars[car_id] = {}

            cars[car_id][field] = value

    root = ET.Element("Cars")

    for car in cars.values():
        car_elem = ET.SubElement(root, "Car")
        for k, v in car.items():
            ET.SubElement(car_elem, k).text = v

    rough = ET.tostring(root, "utf-8")
    pretty = minidom.parseString(rough).toprettyxml(indent="  ")

    with open(OUTPUT_FILE, "w") as f:
        f.write(pretty)

    print("cars.xml file created successfully!")  
    return OUTPUT_FILE


if __name__ == "__main__":
    create_xml_from_txt()