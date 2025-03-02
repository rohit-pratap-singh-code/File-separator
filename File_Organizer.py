import os
import shutil

# Extensions
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"]
video_extensions = [".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv"]
audio_extensions = [".mp3", ".wav", ".aac", ".flac", ".ogg"]
document_extensions = [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"]
compressed_extensions = [".zip", ".rar", ".tar", ".gz"]

print("---> Developer: Rohit Pratap Singh <---")
print("---> File Organizer <---")

def organize_files(source, target, operation="copy"):
    Folders = ["Image", "Video", "Documents", "Audio", "Compressed", "Unknown"]
    for Folder in Folders:
        os.makedirs(os.path.join(target, Folder), exist_ok=True)

    count = 0

    for root, dirs, files in os.walk(source):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1].lower()

            # Determine the destination folder based on file extension
            if file_extension in image_extensions:
                folder = "Image"
            elif file_extension in video_extensions:
                folder = "Video"
            elif file_extension in audio_extensions:
                folder = "Audio"
            elif file_extension in document_extensions:
                folder = "Documents"
            elif file_extension in compressed_extensions:
                folder = "Compressed"
            else:
                folder = "Unknown"

            target_path = os.path.join(target, folder, file)

            try:
                if operation == "copy":
                    shutil.copy(file_path, target_path)
                    print(f"Copied {file} to {folder} folder.")
                elif operation == "move":
                    shutil.move(file_path, target_path)
                    print(f"Moved {file} to {folder} folder.")
                count += 1
            except Exception as e:
                print(f"\033[91mFailed to {operation} {file}. Reason: {e}\033[0m")

    print(f"{count} files successfully {operation}ed.")
    input("Press Enter to exit...")

def main():
    print("1. Copy Files")
    print("2. Move Files")
    print("3. Exit")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in [1, 2]:
                while True:
                    source = input("Enter Source Path: ")
                    if os.path.exists(source):
                        print(f"Source path is valid: {source}")
                        break
                    else:
                        print("Enter a valid source path.")
                
                while True:
                    target = input("Enter Target Path: ")
                    if os.path.exists(target):
                        print(f"Target path is valid: {target}")
                        break
                    else:
                        print("Enter a valid target path.")

                operation = "copy" if choice == 1 else "move"
                organize_files(source, target, operation)

            elif choice == 3:
                exit()
            else:
                print("Invalid Choice")
        except ValueError:
            print("Please enter a valid number.")

main()