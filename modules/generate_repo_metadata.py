import os
import time
from modules.constants import (
    DOCS_FOLDER,
    METADATA_GENERATION_SYSTEM_PROMPT,
    METADATA_GENERATION_HUMAN_PROMPT,
    METADATA_FILE
)
from modules.models import Models
from langchain_core.prompts.chat import ChatPromptTemplate


class RepoMetaDataGenerator:
    def __init__(self, repo_rel_path, src_folder=""):
        self.repo_path = os.path.abspath(repo_rel_path)
        self.src_folder_path = os.path.join(self.repo_path, src_folder)

        # ensure that the docs folder exists
        os.makedirs(DOCS_FOLDER, exist_ok=True)

        # get the model
        models = Models()
        self.model = models.get_metadata_generator_model()

        system_prompt = METADATA_GENERATION_SYSTEM_PROMPT
        human_prompt = "{input}"
        prompt = ChatPromptTemplate.from_messages(
            [("system", system_prompt), ("human", human_prompt)]
        )

        self.chain = prompt | self.model

    def list_all_files(self) -> list:
        print("[INFO] Getting File Paths")
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
        print(f"[INFO] Getting content of {file_path}")
        with open(file_path, "r") as file:
            return file.read()

    def clean_up_file_content(self, file_content: str) -> str:
        print("[INFO] Cleaning up file content")
        return file_content.replace("\n", " ").replace("\t", " ").replace("  ", " ")

    def get_metadata_from_llm(self, file_path: str, file_content: str) -> str:
        print(f"[INFO] Generating metadata for {file_path}")
        query = METADATA_GENERATION_HUMAN_PROMPT.format(
            path=file_path, code=file_content
        )
        response = self.chain.invoke({"input": query})
        content = response.content
        return content

    def get_metadata_of_file(self, file_path: str) -> str:
        file_content = self.get_file_content(file_path)
        metadata = self.get_metadata_from_llm(file_path, file_content)
        return metadata
    
    def generate_metadata(self):
        files = self.list_all_files()
        for file in files:
            metadata = self.get_metadata_of_file(file["file_path_from_here"])
            file["metadata"] = metadata

            # sleep for a second to avoid rate limiting
            time.sleep(1)
        return files
    
    def write_metadata_to_file(self, metadata: list):
        print("[INFO] Writing metadata to file")
        with open(os.path.join(DOCS_FOLDER, METADATA_FILE), "w") as file:
            file.write(str(metadata))
        print("[INFO] Metadata written to file")

    def generate_and_store_metadata(self):
        # if there is the metadata file already, then just return
        if os.path.exists(os.path.join(DOCS_FOLDER, METADATA_FILE)):
            print("[INFO] Metadata already exists")
            return

        metadata = self.generate_metadata()
        self.write_metadata_to_file(metadata)
            
