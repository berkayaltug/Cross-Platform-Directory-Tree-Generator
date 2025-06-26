# ==============================================================
# Project: Cross-Platform Directory Tree Generator
# Author: Berkay Altuğ & ChatGPT (OpenAI)
# Description: Generates a visual, JSON, YAML directory tree.
# License: MIT
# ==============================================================

import os
import sys
import json
import yaml
import datetime
import zipfile

folder_count = -1
file_count = 0
output_lines = []
tree_data = {}  # JSON/YAML data

tab = "|   "
branch = "+-- "

def process_folder(folder_path, prefix="", excludes=None, json_node=None):
    global folder_count, file_count, output_lines

    folder_name = os.path.basename(folder_path)
    folder_count += 1

    exclude_full = False
    exclude_only_content = False

    for excl in excludes:
        if excl.endswith('+') and excl[:-1].lower() == folder_name.lower():
            exclude_only_content = True
        elif excl.lower() == folder_name.lower():
            exclude_full = True

    output_lines.append(f"{prefix}{branch}{folder_name}")
    if json_node is not None:
        json_node[folder_name] = {}

    if exclude_full:
        return
    if exclude_only_content:
        return

    new_prefix = prefix + tab
    current_node = json_node[folder_name] if json_node is not None else None

    try:
        for item in sorted(os.listdir(folder_path)):
            full_path = os.path.join(folder_path, item)
            if os.path.isfile(full_path):
                output_lines.append(f"{new_prefix}{branch}{item}")
                file_count += 1
                if current_node is not None:
                    current_node[item] = None
    except PermissionError:
        output_lines.append(f"{new_prefix}{branch}[Permission Denied]")

    try:
        for item in sorted(os.listdir(folder_path)):
            full_path = os.path.join(folder_path, item)
            if os.path.isdir(full_path):
                process_folder(full_path, new_prefix, excludes, current_node)
    except PermissionError:
        pass

def main():
    global output_lines, tree_data

    # 1. Use CLI argument if provided, else ask user, fallback to cwd
    try:
        if len(sys.argv) > 1:
            inputdir = sys.argv[1]
        else:
            inputdir = input("Enter the directory you'd like to scan: ").strip()
        if not inputdir:
            inputdir = os.getcwd()
    except Exception:
        inputdir = os.getcwd()

    # 2. Validate directory
    if not os.path.exists(inputdir) or not os.path.isdir(inputdir):
        print(f"ERROR: '{inputdir}' does not exist or is not accessible.")
        sys.exit(1)

    # 3. Folder exclusion list
    try:
        exclude_input = input("Enter comma-separated folder names to exclude (use + at end to exclude only contents): ")
    except Exception:
        exclude_input = ""
    excludes = [x.strip() for x in exclude_input.split(",") if x.strip()]

    # 4. Process root folder
    root_name = os.path.basename(os.path.abspath(inputdir))
    tree_data[root_name] = {}
    process_folder(inputdir, "", excludes, tree_data)

    # 5. Prepare text output
    header = [
        "="*60,
        "Cross-Platform Visual Directory Tree Generator (Python)",
        "="*60,
        f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Total folders: {folder_count}",
        f"Total files: {file_count}",
        "="*60,
        ""
    ]
    all_output = header + output_lines
    final_text = "\n".join(all_output)

    # 6. Save output files
    output_dir = os.path.join(os.getcwd(), "output")
    os.makedirs(output_dir, exist_ok=True)
    tree_txt_path = os.path.join(output_dir, "visual_directory_structure.txt")
    json_path = os.path.join(output_dir, "directory_structure.json")
    yaml_path = os.path.join(output_dir, "directory_structure.yaml")
    zip_path = os.path.join(os.getcwd(), "directory_tree_output.zip")

    with open(tree_txt_path, "w", encoding="utf-8") as f:
        f.write(final_text)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(tree_data, f, indent=2)
    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.dump(tree_data, f, allow_unicode=True)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(tree_txt_path, arcname="visual_directory_structure.txt")
        zipf.write(json_path, arcname="directory_structure.json")
        zipf.write(yaml_path, arcname="directory_structure.yaml")

    print(f"\nOutput saved to: {output_dir}")
    print(f"Zipped as: {zip_path}")

    try:
        answer = input("Print output to terminal? (yes/no): ").strip().lower()
        if answer == "yes":
            print("\n" + final_text)
        else:
            print("Saved only to file.")
    except Exception as e:
        print(f"Could not print output: {e}")

if __name__ == "__main__":
    main()