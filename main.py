import os
import modules
from modules.fps_generator import generate_fps
from modules.xml_writer import write_xml

def main(data_path):
    """Main function to orchestrate generating and writing the XML output."""
    fps_element = generate_fps(data_path)
    xml_output_file = os.path.join(data_path, "combined_output.xml")
    write_xml(fps_element, xml_output_file)
    print(f"Generated combined XML file: {xml_output_file}")

if __name__ == "__main__":
    main("data")
