import os
from modules.constants import DOCS_FOLDER


class RepoMetaDataGenerator:
    def __init__(self, repo_rel_path, src_folder=""):
        self.repo_path = os.path.abspath(repo_rel_path)
        self.src_folder_path = os.path.join(self.repo_path, src_folder)

        # ensure that the docs folder exists
        os.makedirs(DOCS_FOLDER, exist_ok=True)

    def list_all_files(self) -> list:
        files = []  # list of tuples containing the relative path (from the root of the folder) and the name of the file

        # the crawl will only happen from the src folder though 
        for root, _, filenames in os.walk(self.src_folder_path):
            for filename in filenames:
                relative_path = os.path.relpath(os.path.join(root, filename), self.repo_path)
                files.append((relative_path, filename))

        return files
       
