from flask import Flask, jsonify, request
from flask_cors import CORS
from modules.code_generator import CodeGenerator
from modules.constants import TARGET_REPO_SRC_FOLDER, TRAGET_REPO_RELATIVE_PATH
from modules.file_detector import FileDetector
from modules.file_evaluator import FileEvaluator
from modules.generate_repo_metadata import RepoMetaDataGenerator
from modules.raise_pr import RaiseGitHubPR


class PRGenerator:
    def __init__(self, prompt):
        self.prompt = prompt
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
        print("Files that could be edited have been detected.")

    def evaluate_files(self):
        file_evaluator = FileEvaluator(self.prompt, self.target_files)
        files = file_evaluator.evaluate_files()
        self.target_files = files
        print("Files have been evaluated.")

    def generate_code(self):
        code_generator = CodeGenerator(self.prompt, self.target_files)
        code = code_generator.generate_code()
        self.target_files = code
        print("Generated code.")

    def raise_pr(self):
        try:
            raise_pr = RaiseGitHubPR(
                self.prompt, TRAGET_REPO_RELATIVE_PATH, self.target_files
            )
            raise_pr.run()
            print("PR raised.")
        except Exception as e:
            print("Error in raising PR. Try again later. The error is: ", e)

    def run(self):
        self.generate_metadata()
        self.detect_files()
        self.evaluate_files()
        self.generate_code()
        self.raise_pr()


# Flak App
app = Flask(__name__)
CORS(app)


# hello route - get request
@app.route("/hello", methods=["GET"])
def hello():
    return "Hello World"


# pr route - post request
@app.route("/create_pr", methods=["POST"])
def create_pr():
    data = request.get_json()

    if not data or "prompt" not in data:
        return jsonify({"message": "No prompt provided"}), 200

    prompt = data["prompt"]

    # strip the prompt, clean it up, and if it is empty, return
    prompt = prompt.strip()
    if not prompt:
        return jsonify({"message": "Prompt is empty"}), 200

    pr_generator = PRGenerator(prompt)
    pr_generator.run()

    return jsonify({"message": "PR has been raised"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
