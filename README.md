# Cross-Platform Visual Directory Tree Generator

## Description

The `Cross-Platform Visual Directory Tree Generator` is a Python-based CLI tool designed to create a structured and visual representation of a directory tree. It recursively scans directories, counts files and folders, generates visual output, and saves the structure in `.txt`, `.json`, `.yaml`, and `.zip` formats.

### Features

- Cross-platform compatibility (Windows, Linux, WSL, macOS).
- Count total number of folders and files.
- Visual tree-style representation.
- Exclude specific folders by name.
- Exclude only contents of folders (with `+` suffix).
- Output formats: plain text, JSON, YAML.
- Generates ZIP archive with all outputs.
- Option to display output in the terminal.

## How to Use

1. **Clone or Download** this repository.

```bash
git clone https://github.com/berkayaltug/Cross-Platform-Directory-Tree-Generator.git
cd cross-platform-directory-tree-generator
```

2. **Install Requirements**:

```bash
pip install -r requirements.txt
```

3. **Run the Script**:

```bash
python directory_tree.py [optional_path]
```

- If no path is provided, you will be prompted.

4. **Exclusions**:

You can exclude folders completely:
```bash
Enter folders to exclude (comma-separated): node_modules,.git,__pycache__
```

Or exclude only their contents:
```bash
Enter folders to exclude content only (use `+`): build+,dist+
```

5. **Output**:
- All outputs (json, yaml, txt) will be saved in an `/output` directory.
- A `.zip` archive (`directory_tree_output.zip`) will include all three formats.
- You will be prompted whether to display the result in the terminal.

---

## Output Example

```
============================================================
Cross-Platform Visual Directory Tree Generator (Python)
============================================================
Generated on: 2025-06-26 15:42:50
Total folders: 10
Total files: 50
============================================================
+-- src
|   +-- main.py
|   +-- utils.py
+-- data
|   +-- dataset.csv
```

---

## Supported Scenarios

| Scenario | Supported |
|---------|-----------|
| Windows, Linux, macOS | ✅ |
| Exclude full folders | ✅ |
| Exclude contents only (`+`) | ✅ |
| CLI arguments | ✅ |
| Manual folder entry | ✅ |
| Outputs: TXT, JSON, YAML, ZIP | ✅ |
| Print to screen (optional) | ✅ |

---

## Requirements

- Python 3.6+
- `pyyaml`

Install dependencies with:
```bash
pip install -r requirements.txt
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more info.

## Orjinal Repo

[**BVisagie**](https://github.com/BVisagie/windows-visual-directory-tree-generator)

## Acknowledgments

- 🛠️ Special thanks to **ChatGPT** and for contributing automation logic and multi-platform design.
