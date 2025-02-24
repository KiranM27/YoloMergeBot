# YoloMergeBot

YoloMergeBot is an application designed to streamline your development workflow by automating minor yet essential code changes. By taking in prompts, YoloMergeBot intelligently analyzes the requirements, modifies the codebase accordingly, and raises a pull request (PR) for review. This automation significantly reduces the manual effort developers typically spend on small tasks, allowing them to focus on more strategic and complex projects. With YoloMergeBot, you can ensure more efficient task management, faster turnaround times for minor changes, and a more productive development environment.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Frontend Setup](#frontend-setup)
  - [Backend Setup](#backend-setup)
  - [Customizing Constants](#customizing-constants)
  - [Indexing the Target Repository](#indexing-the-target-repository)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automates minor code changes based on prompts.
- Modifies the codebase and raises PRs for review.
- Reduces manual effort and increases productivity.
- Ensures faster turnaround times for minor changes.

## Getting Started

### Frontend Setup

The frontend of YoloMergeBot is a Next.js project.

1. Navigate to the `/frontend` directory:

   ```sh
   cd frontend
   ```

2. Install dependencies using Yarn:

   ```sh
   yarn
   ```

3. Run the frontend using:

   ```sh
   yarn dev
   ```

### Backend Setup

The backend of YoloMergeBot is a Python Flask project.

1. Get an OpenAI API key from OpenAI.
2. Copy the .env.template file to create your .env file and store the API key in the .env file:

   ```sh
   cp .env.template .env
   ```

3. Set up the GitHub CLI (gh) and log in by following the [GitHub CLI Quickstart](https://docs.github.com/en/github-cli/github-cli/quickstart).

4. Create a virtual environment and install the dependencies:

   - Follow this [guide](https://medium.com/@KiranMohan27/how-to-create-a-virtual-environment-in-python-be4069ad1efa) to create a virtual environment.
   - Activate the virtual environment and install dependencies:

     ```sh
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     pip install -r requirements.txt
     ```

### Customizing Constants

To customize the backend, you need to modify certain constants in the `backend/modules/constants.py file`. These constants define the repository paths where you want to raise PRs and the folder containing the main source code.

Located in `backend/modules/constants.py` at lines `45-47`, the following constants need to be adjusted:

```python
# repo paths
TARGET_REPO_RELATIVE_PATH = "../../HyperNext"
TARGET_REPO_SRC_FOLDER = "src"
```

Explanation

- `TARGET_REPO_RELATIVE_PATH`: This is the relative path to the GitHub repository where you want to raise the PRs. The path should be relative to the backend folder.
- `TARGET_REPO_SRC_FOLDER`: This is the folder containing the main source code. This path should be relative to the `TARGET_REPO_RELATIVE_PATH`. Ensure that this folder does not include items like node modules or pip libraries.

Adjust these constants as needed to point to your target repository and source folder.


### Indexing the Target Repository

To index the target repository, run the following command to create a document containing the metadata about the target repo:

```python 
python prepare.py
```

This command will generate a file `backend/docs/metadata.json` containing the metadata. Once the metadata is created, format the JSON file for the best experience. Ensure that the JSON is formatted using Prettier or other relevant formatters.


## Usage

Once both the frontend and backend are set up and running, you can start using YoloMergeBot to automate your code changes. Simply provide the necessary prompts, and YoloMergeBot will handle the rest, raising pull requests for your review.

## Contributing

We welcome contributions to YoloMergeBot. If you have suggestions for new features or improvements, feel free to open an issue or submit a pull request.

## License

YoloMergeBot is licensed under the MIT License.
