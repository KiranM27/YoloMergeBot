import os
from modules.constants import DOCS_FOLDER


class RepoMetaDataGenerator:
    def __init__(self, repo_rel_path, src_folder=""):
        self.repo_path = os.path.abspath(repo_rel_path)
        self.src_folder_path = os.path.join(self.repo_path, src_folder)

        # ensure that the docs folder exists
        os.makedirs(DOCS_FOLDER, exist_ok=True)

    def list_all_files(self) -> list:
        files = []  # list of dicts containing
        # the path to the file from the src folder
        # the path to the file from the root of the repo
        # the path to the file from where this code is being executed
        # the file name

        for root, _, file_names in os.walk(self.src_folder_path):
            for file_name in file_names:
                file_path = os.path.join(root, file_name)
                file_path_from_src = os.path.relpath(file_path, self.src_folder_path)
                file_path_from_root = os.path.relpath(file_path, self.repo_path)
                file_path_from_here = os.path.relpath(file_path, os.getcwd())
                files.append(
                    {
                        "file_name": file_name,
                        "file_path_from_src": file_path_from_src,
                        "file_path_from_root": file_path_from_root,
                        "file_path_from_here": file_path_from_here,
                    }
                )

        return files

    def get_file_content(self, file_path: str) -> str:
        with open(file_path, "r") as file:
            return file.read()

    def clean_up_file_content(self, file_content: str) -> str:
        return file_content.replace("\n", " ").replace("\t", " ").replace("  ", " ")
    
    def get_metadata_from_llm(self, file_path: str, file_content: str) -> str:
        pass
    
    def get_metadata(self, file_path: str) -> str:
        file_content = self.get_file_content(file_path)
        file_content = self.clean_up_file_content(file_content)
        return file_content
