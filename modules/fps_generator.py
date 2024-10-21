import os
import xml.etree.ElementTree as ET
import modules
from modules.item_generator import generate_item_from_json


def generate_fps(data_path):
    """Generate the <fps> element based on data in the specified folder."""
    fps = ET.Element("fps")
    generator = ET.SubElement(fps, "generator", name="NJUSTOJ(ACM)", url="http://121.40.211.28/")

    for folder_name in os.listdir(data_path):
        folder_path = os.path.join(data_path, folder_name)
        if os.path.isdir(folder_path):
            json_file = os.path.join(folder_path, "config.json")
            if os.path.exists(json_file):
                json_data = modules.load_json(json_file)
                input_output_files = modules.get_input_output_files(folder_path)
                if input_output_files:
                    item = generate_item_from_json(json_data, input_output_files)
                    fps.append(item)

    return fps
