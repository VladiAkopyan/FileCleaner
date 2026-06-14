from pathlib import Path

def FindFolders(folder_in, folder_type):
    folder_in = Path(folder_in)
    for file in folder_in.rglob(folder_type):
        return file