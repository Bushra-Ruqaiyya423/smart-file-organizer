import os
import shutil

print("================================")
print("     SMART FILE ORGANIZER")
print("================================")

# Ask the user for the folder to organize
folder = input("\nEnter the folder path: ").strip()

# Check whether the folder exists
if not os.path.exists(folder):
    print("\n❌ Folder does not exist!")
    exit()

# File categories
categories = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif",
        ".bmp", ".webp", ".svg"
    ],

    "Documents": [
        ".pdf", ".docx", ".doc", ".txt",
        ".pptx", ".ppt", ".xlsx", ".xls",
        ".csv"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov",
        ".wmv", ".flv"
    ],

    "Audio": [
        ".mp3", ".wav", ".m4a", ".aac",
        ".flac", ".ogg"
    ],

    "Archives": [
        ".zip", ".rar", ".7z", ".tar",
        ".gz"
    ],

    "Code": [
        ".py", ".java", ".c", ".cpp",
        ".html", ".css", ".js", ".sql"
    ]
}

# Counters for summary
moved_files = 0
category_count = {}

# Go through every item in the folder
for filename in os.listdir(folder):

    file_path = os.path.join(folder, filename)

    # Ignore folders
    if os.path.isdir(file_path):
        continue

    # Get file extension
    extension = os.path.splitext(filename)[1].lower()

    category_found = False

    # Find the correct category
    for category, extensions in categories.items():

        if extension in extensions:

            category_folder = os.path.join(folder, category)

            # Create the category folder
            os.makedirs(category_folder, exist_ok=True)

            destination = os.path.join(
                category_folder,
                filename
            )

            # Move the file
            shutil.move(file_path, destination)

            print(f"✓ Moved {filename} → {category}")

            moved_files += 1
            category_count[category] = category_count.get(category, 0) + 1

            category_found = True
            break

    # Unknown file types
    if not category_found:

        category_folder = os.path.join(folder, "Others")

        os.makedirs(category_folder, exist_ok=True)

        destination = os.path.join(
            category_folder,
            filename
        )

        shutil.move(file_path, destination)

        print(f"✓ Moved {filename} → Others")

        moved_files += 1
        category_count["Others"] = category_count.get("Others", 0) + 1


# Final summary
print("\n================================")
print("       ORGANIZATION COMPLETE")
print("================================")

print(f"\nTotal files organized: {moved_files}")

for category, count in category_count.items():
    print(f"{category}: {count}")

print("\n✓ Done!") 