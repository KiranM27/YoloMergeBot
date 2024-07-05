from modules.constants import TRAGET_REPO_RELATIVE_PATH, TARGET_REPO_SRC_FOLDER
from modules.generate_repo_metadata import RepoMetaDataGenerator
from modules.file_detector import FileDetector
from pprint import pprint


class Runner:
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
        prompt = 'Make the default mode of the app dark.'
        file_detector = FileDetector(prompt)
        files = file_detector.detect_files()
        print("The files that potentially need to be edited are: ")
        pprint(files)


if __name__ == "__main__":
    runner = Runner()
    runner.generate_metadata()
    runner.detect_files()
