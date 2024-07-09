import json
from modules.models import Models
from modules.file_helpers import FileHelpers
from modules.constants import (
    FILE_EVALUATION_SYSTEM_PROMPT,
    FILE_EVALUATION_HUMAN_PROMPT,
)
from langchain_core.prompts.chat import ChatPromptTemplate


class FileEvaluator:
    def __init__(self, user_query: str, target_files: list):
        models = Models()
        self.model = models.get_file_evaluation_model()
        self.user_query = user_query

        # create the prompt
        system_prompt = FILE_EVALUATION_SYSTEM_PROMPT
        human_prompt = "{input}"
        prompt = ChatPromptTemplate.from_messages(
            [("system", system_prompt), ("human", human_prompt)]
        )

        self.chain = prompt | self.model

        file_helpers = FileHelpers()

        for target_file in target_files:
            # use the file_path_from_here to get the content of the file
            file_path = target_file["file_path_from_here"]
            file_content = file_helpers.get_file_content(file_path)
            target_file["code"] = file_content

        self.metadata = target_files

    def evaluate_files(self):
        query = FILE_EVALUATION_HUMAN_PROMPT.format(
            input=self.user_query, metadata=self.metadata
        )
        response = self.chain.invoke({"input": query})
        content = response.content

        # parse the content into a list of dicts
        content = json.loads(content)
        return content
