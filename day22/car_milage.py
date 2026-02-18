import xml.etree.ElementTree as ET

def push_data_to_xml(source_file, output_file):
    # 1. Read the data from the text file
    data_dict = {}
    
    try:
        with open(source_file, 'r') as f:
            for line in f:
                # Split by colon and strip whitespace
                if ':' in line:
                    key, value = line.split(':', 1)
                    data_dict[key.strip()] = value.strip()
                    
        if not data_dict:
            print("No data found in the text file.")
            return

        # Create the XML structure
        root = ET.Element("VehicleDetails")
        
        # Iterate through the dictionary to create XML sub-elements
        for key, value in data_dict.items():
            child = ET.SubElement(root, key)
            child.text = value

        # 3. Write to the XML file
        tree = ET.ElementTree(root)
        
        # Using encoding='utf-8' and xml_declaration=True for a standard XML header
        tree.write(output_file, encoding='utf-8', xml_declaration=True)
        
        print(f"Successfully pushed data from {source_file} to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{source_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    source_file = 'D:\Wipro Training\python-automotive-batch9\day22\data1.txt'
    push_data_to_xml(source_file, 'vehicle_data.xml')