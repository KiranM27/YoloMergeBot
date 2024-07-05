OPEN_AI_API_KEY = 'OPEN_AI_API_KEY' # the key used to access the openai api key in the .env file

# this has access to the internet but its not the most powerful model out there
OPEN_AI__METADATA_GENERATION_MODEL = 'gpt-3.5-turbo-0125' # models - https://platform.openai.com/docs/models
OPEN_AI_FILE_DETECTION_MODEL = 'gpt-4o'
OPEN_AI_CODE_GENERATION_MODEL = 'gpt-4o'

# prompts 
# does not really give an entire paragraph, but might as well put it in the prompt 
METADATA_GENERATION_SYSTEM_PROMPT = 'You are a helpful assistant that helps generate metadata for the files in a GitHub repository. The repository is called HyperNext, which is a template for a next js project. The goal is to eventually use the metadata that is generated to identify which files to look at when we want to make a specific change to the codebase of the project. So the descriptions that you generate should be informative and concise, since we want to reduce the look-up time. You should return only stictly return only the description of the file and nothing else.'
METADATA_GENERATION_HUMAN_PROMPT = "The Path and Code from the file. Path: {path}. Code: {code}"

# temperatures 
OPEN_AI_MODEL_TEMPERATURE = 0.5

# data folder
DATA_FOLDER = 'data'
DOCS_FOLDER = 'docs'

# repo paths 
TRAGET_REPO_RELATIVE_PATH = '../HyperNext'
TARGET_REPO_SRC_FOLDER = 'src'