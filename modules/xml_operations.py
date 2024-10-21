import xml.etree.ElementTree as ET
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element, including the XML declaration."""
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ")
    return f'<?xml version="1.0" encoding="UTF-8"?>\n' + '\n'.join(pretty_xml.splitlines()[1:])

def replace_html_entities(xml_string):
    """Replace HTML entities with their original characters."""
    return xml_string.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
