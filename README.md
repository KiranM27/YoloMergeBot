# YoloMergeBot

YoloMergeBot is an application designed to streamline your development workflow by automating minor yet essential code changes. By taking in prompts, YoloMergeBot intelligently analyzes the requirements, modifies the codebase accordingly, and raises a pull request (PR) for review. This automation significantly reduces the manual effort developers typically spend on small tasks, allowing them to focus on more strategic and complex projects. With YoloMergeBot, you can ensure more efficient task management, faster turnaround times for minor changes, and a more productive development environment.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Frontend Setup](#frontend-setup)
  - [Backend Setup](#backend-setup)
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

## Backend Setup

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

## Usage

Once both the frontend and backend are set up and running, you can start using YoloMergeBot to automate your code changes. Simply provide the necessary prompts, and YoloMergeBot will handle the rest, raising pull requests for your review.

## Contributing

We welcome contributions to YoloMergeBot. If you have suggestions for new features or improvements, feel free to open an issue or submit a pull request.

## License

YoloMergeBot is licensed under the MIT License.
