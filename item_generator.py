import xml.etree.ElementTree as ET
import modules
import base64
import re
import time
from xml.etree.ElementTree import Element, SubElement


def extract_and_replace_base64(content):
    """提取base64编码的图片并替换为<img>标签，同时返回完整的图片信息."""
    # 定义正则匹配base64图片的模式
    base64_pattern = r'data:image/(png|jpg|jpeg);base64,([A-Za-z0-9+/=]+)'
    img_info_list = []

    # 替换base64编码为<img src>标签
    def replace_match(match):
        img_type = match.group(1)  # 获取图片类型
        base64_data = match.group(2)  # 获取base64数据
        timestamp = time.strftime('%Y%m%d%H%M%S')  # 按时间生成文件名的一部分
        unique_id = base64.urlsafe_b64encode(base64_data[:6].encode('utf-8')).decode('utf-8')[:6]  # 生成唯一ID
        filename = f"/storage/ckeditor/images/{time.strftime('%Y%m%d')}/{timestamp}_{unique_id}.{img_type}"
        img_info_list.append((filename, base64_data))
        return f'{filename}'  # 确保只返回正确的 img 标签

    # 处理内容，将匹配的base64编码替换为<img>标签
    updated_content = re.sub(base64_pattern, replace_match, content)

    return updated_content, img_info_list



def generate_item_from_json(json_data, input_output_files, folder_name):
    """Generate a single <item> element based on JSON data and input/output test files."""
    item = ET.Element("item")

    title = ET.SubElement(item, "title")
    title.text = f"<![CDATA[{json_data['title']}]]>"

    time_limit = ET.SubElement(item, "time_limit", unit="ms")
    time_limit.text = f"<![CDATA[{json_data['timelimit']}]]>"

    memory_limit = ET.SubElement(item, "memory_limit", unit="mb")
    memory_limit.text = f"<![CDATA[{modules.convert_memory(json_data['memorylimit'])}]]>"

    description = ET.SubElement(item, "description")

    # 原来的description文本替换换行符为<br>
    description_text = modules.replace_newlines_with_br(json_data['description'])

    # 使用extract_and_replace_base64处理base64编码的图片
    updated_description, base64_images = extract_and_replace_base64(description_text)

    # 将替换后的description内容放入XML中
    description.text = f"<![CDATA[{updated_description}]]>"

    # 处理 base64 图片，将它们添加到item末尾
    for img_filename, base64_data in base64_images:
        img_element = ET.SubElement(item, "img")
        src_element = ET.SubElement(img_element, "src")
        src_element.text = f"<![CDATA[{img_filename}]]>"

        base64_element = ET.SubElement(img_element, "base64")
        base64_element.text = f"<![CDATA[{base64_data}]]>"

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
