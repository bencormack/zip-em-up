# zip-em-up
This Python script automates the process of individually zipping HTML banner ads. It scans the current working directory for HTML files, identifies their parent and current directory names, and creates separate ZIP archives for each banner inside a `ZIPs` folder.

## Prerequisites

Before using this script, ensure you have:

- **Python 3.6+** (recommended)

No additional dependencies are required as the script only uses built-in Python libraries.

## How It Works

1. The script scans the current directory and subdirectories for `.html` files.
2. When an HTML file is found, it determines the banner's folder structure.
3. It creates a ZIP archive named `{parent_folder}_{current_folder}.zip`.
4. The ZIP archive includes all files from the detected banner directory.
5. All ZIP files are stored in a `ZIPs` directory within the script's location.

## Usage

To run the script, simply execute:

```sh
python script.py
```

This will create ZIP files for all banners found and store them in the `ZIPs` folder.

## Notes

- The script ensures each banner directory is only processed **once**, even if multiple HTML files exist inside it.
- The ZIP file name is derived from the **parent directory** and **current directory** to provide clear identification.
- If the `ZIPs` folder does not exist, the script will create it automatically.

## Troubleshooting

- **No ZIP files created**: Ensure you are running the script in a directory containing HTML banner ads.
- **Duplicate ZIPs or missing files**: Verify that each banner has a unique parent directory and that all relevant files are stored within the banner folder.
- **Permission issues**: If running on a restricted system, ensure the script has write permissions to the `ZIPs` directory.

## License

This script is provided "as is" without any warranties. Feel free to modify and adapt it for your use case.

