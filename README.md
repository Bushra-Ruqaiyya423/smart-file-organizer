# Smart File Organizer 📁

A Python-based automation tool that organizes files into categories based on their file extensions.

## 🚀 Features

* Automatically detects file extensions
* Organizes files into appropriate folders
* Creates category folders automatically
* Supports images, documents, videos, audio, archives and code files
* Handles unknown file types using an `Others` category
* Displays a summary of organized files

## 🛠️ Technologies Used

* Python
* OS module
* Shutil module

## 📂 Supported Categories

| Category  | Examples                             |
| --------- | ------------------------------------ |
| Images    | JPG, PNG, GIF, SVG, WEBP             |
| Documents | PDF, DOCX, TXT, PPTX, XLSX, CSV      |
| Videos    | MP4, MKV, AVI, MOV                   |
| Audio     | MP3, WAV, M4A, AAC, FLAC             |
| Archives  | ZIP, RAR, 7Z, TAR                    |
| Code      | PY, JAVA, C, CPP, HTML, CSS, JS, SQL |
| Others    | Unsupported file types               |

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Open the project

```bash
cd Smart-File-Organizer
```

### 3. Run the program

```bash
python organizer.py
```

### 4. Enter the folder path

When prompted, enter the path of the folder you want to organize.

Example:

```text
C:\Users\YourName\Documents\Test-Folder
```

## 📌 Example

### Before

```text
Test-Folder/
├── photo.png
├── assignment.pdf
├── video.mp4
├── song.mp3
└── program.py
```

### After

```text
Test-Folder/
├── Images/
│   └── photo.png
├── Documents/
│   └── assignment.pdf
├── Videos/
│   └── video.mp4
├── Audio/
│   └── song.mp3
└── Code/
    └── program.py
```

## 🔮 Future Improvements

* Add a graphical user interface
* Add a preview/dry-run mode
* Add duplicate-file detection
* Add customizable categories
* Add logging functionality
## Project Status
Completed✅

## 👨‍💻 Author
|Computer Science Engineering Student | Python & Software Development Enthusiast | Building Projects & Exploring Technology |
