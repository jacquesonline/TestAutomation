import os
from pathlib import Path

SUBDIRECTORIES = {
    "Documents": ['.pdf','.rtf','.txt'],
    "Audio": ['.m4a','.m4b','.mp3'],
    "Videos": ['.mov','.avi','.mp4'],
    "Images": ['.jpg','.jpeg','.png'],
    "Programs" : ['.py']
}

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        if value in suffixes:
            return category
    return "MISC"

# test out the pickDirectory() function
# print(pickDirectory(".pdf"))

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDirectory(fileType)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

# test out the organizeDirectory() function
organizeDirectory()