import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from modules.constants import (
    OPEN_AI_API_KEY,
    OPEN_AI_MODEL_TEMPERATURE,
    OPEN_AI__METADATA_GENERATION_MODEL,
    OPEN_AI_FILE_DETECTION_MODEL
)

load_dotenv()  # take environment variables from .env.


class Models:
    def __init__(self):
        open_ai_api_key = os.getenv(OPEN_AI_API_KEY)
        self.open_ai_api_key = open_ai_api_key

    def get_metadata_generator_model(self):
        model = ChatOpenAI(
            temperature=OPEN_AI_MODEL_TEMPERATURE,
            model_name=OPEN_AI__METADATA_GENERATION_MODEL,
            openai_api_key=self.open_ai_api_key,
        )

        return model

    def get_file_detection_model(self):
        model = ChatOpenAI(
            temperature=OPEN_AI_MODEL_TEMPERATURE,
            model_name=OPEN_AI_FILE_DETECTION_MODEL,
            openai_api_key=self.open_ai_api_key,
        )

        return model
