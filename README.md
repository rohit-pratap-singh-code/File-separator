# File Organizer

## Overview
A Python-based file organizer that automatically sorts files into categorized folders (Images, Videos, Documents, Audio, and Compressed) based on their extensions. It allows users to **copy** or **move** files from a source directory to a target directory.

## Features
- Organizes files into predefined categories:
  - **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg`
  - **Videos**: `.mp4`, `.avi`, `.mov`, `.mkv`, `.wmv`, `.flv`
  - **Audio**: `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`
  - **Documents**: `.pdf`, `.doc`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.csv`
  - **Compressed**: `.zip`, `.rar`, `.tar`, `.gz`
  - **Unknown**: Files that do not match the above categories
- **Copy** or **Move** files based on user preference
- Handles errors gracefully and informs the user of any issues
- Simple command-line interface

## Installation
### Prerequisites
Ensure you have Python installed on your system. You can check by running:
```sh
python --version
```

### Clone the Repository
```sh
git clone https://github.com/your-username/file-organizer.git
cd file-organizer
```

## Usage
Run the script using:
```sh
python file_organizer.py
```
Follow the on-screen instructions to select your operation (**Copy** or **Move**) and provide source and target directories.

## Example
1. Run the script.
2. Choose an operation:
   - `1` for Copy
   - `2` for Move
3. Enter the source folder path.
4. Enter the target folder path.
5. The script will process the files and organize them into respective folders.

## Developer
**Rohit Pratap Singh**

## Contributing        
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

