import os
import modules

def write_xml(fps_element, output_file):
    """Write the final XML to a file in Unix format (LF)."""
    xml_string = modules.prettify(fps_element)
    xml_string = modules.replace_html_entities(xml_string)

    # 确保写入文件时是 Unix 换行符
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        f.write(xml_string.replace('\r\n', '\n'))
