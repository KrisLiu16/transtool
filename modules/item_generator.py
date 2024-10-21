import xml.etree.ElementTree as ET
import modules


def generate_item_from_json(json_data, input_output_files):
    """Generate a single <item> element based on JSON data and input/output test files."""
    item = ET.Element("item")

    title = ET.SubElement(item, "title")
    title.text = f"<![CDATA[{json_data['title']}]]>"

    time_limit = ET.SubElement(item, "time_limit", unit="ms")
    time_limit.text = f"<![CDATA[{json_data['timelimit']}]]>"

    memory_limit = ET.SubElement(item, "memory_limit", unit="mb")
    memory_limit.text = f"<![CDATA[{modules.convert_memory(json_data['memorylimit'])}]]>"

    description = ET.SubElement(item, "description")
    description_text = modules.replace_newlines_with_br(json_data['description'])
    description.text = f"<![CDATA[{description_text}]]>"

    input_desc = ET.SubElement(item, "input")
    input_text = modules.replace_newlines_with_br(json_data['inputdescription'])
    input_desc.text = f"<![CDATA[{input_text}]]>"

    output_desc = ET.SubElement(item, "output")
    output_text = modules.replace_newlines_with_br(json_data['outputdescription'])
    output_desc.text = f"<![CDATA[{output_text}]]>"

    # 处理示例
    input_samples = modules.extract_sample_content(json_data.get('inputsample', ''))
    output_samples = modules.extract_sample_content(json_data.get('outputsample', ''))

    for input_sample, output_sample in zip(input_samples, output_samples):
        sample_input = ET.SubElement(item, "sample_input")
        sample_input.text = f"<![CDATA[{input_sample}]]>"

        sample_output = ET.SubElement(item, "sample_output")
        sample_output.text = f"<![CDATA[{output_sample}]]>"

    # 处理 test_input 和 test_output 文件
    for idx, (input_file, output_file) in enumerate(input_output_files):
        test_input = ET.SubElement(item, "test_input", filename=f"{idx}.in")
        with open(input_file, 'r', encoding='utf-8') as infile:
            test_input.text = f"<![CDATA[{infile.read().strip()}]]>"

        test_output = ET.SubElement(item, "test_output", filename=f"{idx}.out")
        with open(output_file, 'r', encoding='utf-8') as outfile:
            test_output.text = f"<![CDATA[{outfile.read().strip()}]]>"

    return item
