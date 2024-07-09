from modules.constants import TRAGET_REPO_RELATIVE_PATH, TARGET_REPO_SRC_FOLDER
from modules.generate_repo_metadata import RepoMetaDataGenerator
from modules.file_detector import FileDetector
from modules.code_generator import CodeGenerator
from pprint import pprint


class Runner:
    def __init__(self):
        self.prompt = "Make the default mode of the app dark."
        self.target_files = []

    def generate_metadata(self):
        repo_metadata_generator = RepoMetaDataGenerator(
            TRAGET_REPO_RELATIVE_PATH, TARGET_REPO_SRC_FOLDER
        )
        files = repo_metadata_generator.list_all_files()

        if not files:
            print("No files found in the repo")
            return

        repo_metadata_generator.generate_and_store_metadata()

    def detect_files(self):
        file_detector = FileDetector(self.prompt)
        files = file_detector.detect_files()
        self.target_files = files
        print("Files to be edited:")
        pprint(files)

    def generate_code(self):
        code_generator = CodeGenerator(self.prompt, self.target_files)
        code = code_generator.generate_code()
        print("Generated code:")
        pprint(code)


if __name__ == "__main__":
    runner = Runner()
    runner.generate_metadata()
    runner.detect_files()
    runner.generate_code()
