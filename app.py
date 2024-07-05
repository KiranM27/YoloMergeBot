from modules.constants import TRAGET_REPO_RELATIVE_PATH, TARGET_REPO_SRC_FOLDER
from modules.generate_repo_metadata import RepoMetaDataGenerator
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

        file = files[0]
        file_path = file["file_path_from_here"]
        file_content = repo_metadata_generator.get_file_content(file_path)
        pprint(file_content)


if __name__ == "__main__":
    runner = Runner()
    runner.generate_metadata()
