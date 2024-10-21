import os

def get_input_output_files(folder_path):
    """Retrieve all input/output files in a folder."""
    input_output_files = []
    idx = 0
    while True:
        input_file = os.path.join(folder_path, f"{idx}.in")
        output_file = os.path.join(folder_path, f"{idx}.out")
        if os.path.exists(input_file) and os.path.exists(output_file):
            input_output_files.append((input_file, output_file))
            idx += 1
        else:
            break
    return input_output_files
