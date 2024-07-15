OPEN_AI_API_KEY = (
    "OPEN_AI_API_KEY"  # the key used to access the openai api key in the .env file
)

GPT_3_5_MODEL = "gpt-3.5-turbo-0125"  # models - https://platform.openai.com/docs/models

OPEN_AI__METADATA_GENERATION_MODEL = GPT_3_5_MODEL
OPEN_AI_FILE_DETECTION_MODEL = GPT_3_5_MODEL
OPEN_AI_CODE_GENERATION_MODEL = GPT_3_5_MODEL
OPEN_AI_FILE_EVALUATION_MODEL = GPT_3_5_MODEL
OPEN_AI_CODE_GENERATION_MODEL = GPT_3_5_MODEL

# information about the repo
TARGET_REPO_INFORMATION = (
    "The repository is called HyperNext, which is a template for a next js project"
)

# prompts
METADATA_GENERATION_SYSTEM_PROMPT = f"You are a helpful assistant that helps generate metadata for the files in a GitHub repository. {TARGET_REPO_INFORMATION} . The goal is to eventually use the metadata that is generated to identify which files to look at when we want to make a specific change to the codebase of the project. So the descriptions that you generate should be informative and concise, since we want to reduce the look-up time. You should return only stictly return only the description of the file and nothing else."
METADATA_GENERATION_HUMAN_PROMPT = (
    "The Path and Code from the file. Path: {path}. Code: {code}"
)


# file detection prompts
FILE_DETECTION_SYSTEM_PROMPT = f"You are a helpful assistant that helps identify the files that need to be edited in a GitHub repository. {TARGET_REPO_INFORMATION}. Given an input prompt, you should take a look at the metadata of the files in the repository and return a list of objects corresponding to the files that need to be edited. You can return a list of potential file objects that might have to be edited. We will go over the files again to double check which of the files needs to be edited. Only return the list of objects and nothing else. The response should be a list of dicts with the keys file_name, file_path_from_src, file_path_from_root, file_path_from_here. Take the keys from the metadata that is passed in and return the same ones in the response. DO NOT MAKE ANY CHANGES TO THE METADATA. The output does not need to be in a code block as well. Just in text format, but wiht a list of objects is good. FOR THE RESPONSE, ENCASE ALL THE STRINGS IN THE JSON LIST / OBJECT IN DOUBLE QUOTES SINCE SINGLE QUOTES ARE NOT ALLOWED IN JSON."
FILE_DETECTION_HUMAN_PROMPT = "The prompt that you should use to identify the files that need to be edited is: {input}, the metadata: {metadata}"

# file evaluation prompts
FILE_EVALUATION_SYSTEM_PROMPT = f"You are a helpful assistant that helps evaluate the files in a GitHub repository. {TARGET_REPO_INFORMATION}. Given an input prompt, and the content of a few files, you should decide which files need to be edited to achieve the objective of the prompt. You should return a list of objects that have the following keys: file_name, file_path_from_src, file_path_from_root, file_path_from_here. The output does not need to be in a code block as well. Just in text format, but with a list of objects is good. FOR THE RESPONSE, ENCASE ALL THE STRINGS IN THE JSON LIST / OBJECT IN DOUBLE QUOTES SINCE SINGLE QUOTES ARE NOT ALLOWED IN JSON. Your role is to identify the smallest subset of files that need to be edited and return them. Only return the files that need to be edited and you can discard the rest. You should return a list at all times. If there no files to be edited, return an empty list."
FILE_EVALUATION_HUMAN_PROMPT = "The prompt that you should use to evaluate the files is: {input}, the metadata: {metadata}"

# code generation prompts
CODE_GENERATION_SYSTEM_PROMPT = f"You are a helpful assistant that helps generate code for a GitHub repository. {TARGET_REPO_INFORMATION}. Given an input prompt, and the content of a few files, you should decide how to achieve the objective of the prompt whilst editing as few files as possible, while writing clean code. You should return a list of objects that have the following keys: file_name, file_path_from_src, file_path_from_root, file_path_from_here, was_edited, code. If the file was edited, set the was_edited field to true and if not, you can just set it to false. IF AN EDIT WAS MADE TO THE CODE IN A FILE, SET THE was_edited FIELD TO BE TRUE AND RETURN THE CONTENT OF THE WHOLE EDITED FILE AND NOT JUST THE EDITED PORTION. For the code field, you can return an empty string if the code was not edited. The output does not need to be in a code block as well. Just in text format, but with a list of objects is good. FOR THE RESPONSE, ENCASE ALL THE STRINGS IN THE JSON LIST / OBJECT IN DOUBLE QUOTES SINCE SINGLE QUOTES ARE NOT ALLOWED IN JSON. Be very thorough with the code that is being returned since that is what will be used to make the changes in the repository. So ensure that the code is right and takes care of all edge cases."
CODE_GENERATION_HUMAN_PROMPT = "The prompt that you should use to generate code is: {input}, the metadata: {metadata}. RETURN THE ENTIRE FILE CONTENT IF AN EDIT WAS MADE TO THE FILE. DO NOT RETURN JUST THE EDITED PORTION."

# temperatures
OPEN_AI_MODEL_TEMPERATURE = 0.5

# data folder
DATA_FOLDER = "data"
DOCS_FOLDER = "docs"
METADATA_FILE = "metadata.json"

# repo paths
TARGET_REPO_RELATIVE_PATH = "../../HyperNext"
TARGET_REPO_SRC_FOLDER = "src"
