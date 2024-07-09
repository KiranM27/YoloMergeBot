import os
import random
import string
from modules.file_helpers import FileHelpers


class RaiseGitHubPR:
    def __init__(self, prompt: str, target_repo_path: str, target_files: list):
        self.prompt = prompt
        self.target_repo_path = target_repo_path
        self.target_files = target_files

    # name generato for the branch
    # the naming convention for now will be ai-pr/{random_string_10_chars}
    def get_branch_name(self):
        choices = string.ascii_lowercase + string.digits
        random_string = "".join(random.choices(choices, k=10))
        branch_name = f"ai-pr/{random_string}"
        return branch_name

    def cd_to_target_repo(self):
        os.chdir(self.target_repo_path)

    # use a different terminal instance to run commands
    # such as creating a new branch
    def create_branch(self, branch_name):
        os.system(f"git checkout -b {branch_name}")

    def replace_the_files_in_repo(self):
        file_helpers = FileHelpers()

        for target_file in self.target_files:
            was_edited = target_file["was_edited"]
            if not was_edited:
                continue
            file_path = target_file["file_path_from_here"]
            file_content = target_file["code"]
            file_helpers.store_file_content(file_path, file_content)

    def commit_files(self):
        os.system("git add .")
        os.system("git commit -m 'feat: AI Automated Code Change'")

    def push_to_github(self, branch_name):
        os.system(f"git push origin {branch_name}")

    def raise_pr(self):
        pr_description = f"This PR was created by an AI. The prompt was: {self.prompt}"
        os.system(
            f"gh pr create --title 'AI Automated PR' --body '{pr_description}' --base main"
        )

    def run(self):
        branch_name = self.get_branch_name()
        self.cd_to_target_repo()
        self.create_branch(branch_name)
        self.replace_the_files_in_repo()
        self.commit_files()
        self.push_to_github(branch_name)
        self.raise_pr()
