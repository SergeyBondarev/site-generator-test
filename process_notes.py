import os
import subprocess

INPUT_DIR = "./markdown_files"
OUTPUT_DIR = "./processed_files"

def process_latex(file_path):
    output_path = os.path.join(OUTPUT_DIR, os.path.basename(file_path))
    subprocess.run([
        "pandoc",
        file_path,
        "-o", output_path,
        "--mathjax"
    ])

if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for root, _, files in os.walk(INPUT_DIR):
        for file in files:
            if file.endswith(".md"):
                process_latex(os.path.join(root, file))

