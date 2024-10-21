import xml.etree.ElementTree as ET
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element, including the XML declaration."""
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ")
    return f'<?xml version="1.0" encoding="UTF-8"?>\n' + '\n'.join(pretty_xml.splitlines()[1:])


def replace_html_entities(xml_string):
    """替换所有HTML转义字符为其原始字符."""
    replacements = {
        "&quot;": '"',
        "&apos;": "'",
        "&lt;": "<",
        "&gt;": ">",
        "&amp;": "&",
        "&nbsp;": " ",
        "&cent;": "¢",
        "&pound;": "£",
        "&yen;": "¥",
        "&euro;": "€",
        "&copy;": "©",
        "&reg;": "®",
        "&trade;": "™",
        "&bull;": "•",
        "&hellip;": "…",
        "&mdash;": "—",
        "&ndash;": "–",
        "&lsquo;": "‘",
        "&rsquo;": "’",
        "&ldquo;": "“",
        "&rdquo;": "”",
        "&tilde;": "˜",
        "&mdash;": "—",
        "&nbsp;": " ",
        # 可以根据需要添加更多转义字符
    }

    for escaped, original in replacements.items():
        xml_string = xml_string.replace(escaped, original)

    return xml_string

