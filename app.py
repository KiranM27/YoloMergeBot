from modules.constants import TRAGET_REPO_RELATIVE_PATH, TARGET_REPO_SRC_FOLDER
from modules.generate_repo_metadata import RepoMetaDataGenerator
from pprint import pprint


def runner():
    repo_metadata_generator = RepoMetaDataGenerator(TRAGET_REPO_RELATIVE_PATH, TARGET_REPO_SRC_FOLDER)
    files = repo_metadata_generator.list_all_files()
    pprint(files)


if __name__ == "__main__":
    runner()
