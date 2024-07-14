import os
from modules.constants import DOCS_FOLDER, METADATA_FILE


class FileHelpers:

    def __init__(self):
        # ensure that the docs folder exists
        os.makedirs(DOCS_FOLDER, exist_ok=True)

    def get_metadata_file_path(self) -> str:
        return os.path.join(DOCS_FOLDER, METADATA_FILE)

    def get_file_content(self, file_path: str) -> str:
        print(f"[INFO] Getting content of {file_path}")
        with open(file_path, "r") as file:
            return file.read()

    def store_file_content(self, file_path: str, content: str):
        print(f"[INFO] Storing content in {file_path}")
        
        # get the current working directory
        cwd = os.getcwd()
        print("cwd: ", cwd) 
        with open(file_path, "w") as file:
            file.write(content)
