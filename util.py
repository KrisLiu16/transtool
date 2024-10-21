import re

def convert_memory(memory_kb):
    """Convert memory limit from KB to MB."""
    return str(int(memory_kb) // 1024)

def replace_newlines_with_br(text):
    """Replace newline characters with <br> for HTML display."""
    return text.replace("\n", "<br>")

def extract_sample_content(sample_text):
    """Extract sample contents by splitting on '样例' and cleaning text."""
    samples = sample_text.split("样例")
    extracted_contents = []
    for sample in samples:
        clean_sample = re.sub(r'[123456789一二三四五六七八九][：:]', '', sample)
        clean_sample = re.sub(r'<.*?>', '', clean_sample).strip()
        if clean_sample:
            extracted_contents.append(clean_sample)
    return extracted_contents
