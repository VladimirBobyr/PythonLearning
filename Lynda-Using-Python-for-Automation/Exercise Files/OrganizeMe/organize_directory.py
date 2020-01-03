import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt','.docx'],
    "AUDIO": ['.m3a','.m4a','.mp3','.wav'],
    "VIDEO": ['.mov','.avi','.mp4','.mpeg'],
    "IMAGES": ['.jpg','.jpeg','.png','.bmp']
}

def getDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'

#print(getDirectory('.pdf'))

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = getDirectory(filetype)
        directoryPath = Path(directory)
        # Create directory in case it doesn't exist
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        # Moving file
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()




