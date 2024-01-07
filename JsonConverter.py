import json
import xml.etree.ElementTree as ET

def json_to_xml(input_file, output_file):
    try:
        with open(input_file, 'r') as json_file:
            data = json.load(json_file)
    except json.decoder.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return

    root = ET.Element("root")

    def build_xml(element, data):
        if isinstance(data, dict):
            for key, value in data.items():
                child = ET.Element(key)
                element.append(child)
                build_xml(child, value)
        elif isinstance(data, list):
            for item in data:
                child = ET.Element("item")
                element.append(child)
                build_xml(child, item)
        else:
            element.text = str(data)

    build_xml(root, {'root': data})  # Wrap top-level array in a dictionary

    tree = ET.ElementTree(root)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    input_file = "Wiki.json"
    output_file = "Output.xml"

    json_to_xml(input_file, output_file)

    print(f"Conversion successful. XML file saved at {output_file}")
