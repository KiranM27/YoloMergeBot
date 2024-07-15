
from modules.constants import TARGET_REPO_SRC_FOLDER, TRAGET_REPO_RELATIVE_PATH
from modules.generate_repo_metadata import RepoMetaDataGenerator


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

    def run(self):
        self.generate_metadata()


if __name__ == "__main__":
    runner = Runner()
    runner.run()
