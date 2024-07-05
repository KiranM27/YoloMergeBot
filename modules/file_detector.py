# take in a prompt and using the metadata stored in the json file 
# find the files that need to be edited 
# once the files are found, look at the file's content and see if it makes sense 
# and also pull any other files that are related to the file that needs to be edited

import json
from modules.models import Models
from modules.file_helpers import FileHelpers
from modules.constants import FILE_DETECTION_SYSTEM_PROMPT, FILE_DETECTION_HUMAN_PROMPT
from langchain_core.prompts.chat import ChatPromptTemplate


class FileDetector:
    def __init__(self, user_query: str):

        models = Models()
        self.model = models.get_file_detection_model()
        self.user_query = user_query

        # create the prompt
        system_prompt = FILE_DETECTION_SYSTEM_PROMPT        
        human_prompt = "{input}"
        prompt = ChatPromptTemplate.from_messages(
            [("system", system_prompt), ("human", human_prompt)]
        )

        self.chain = prompt | self.model

        # fetch the metadata from the json file
        self.file_helpers = FileHelpers()
        metadata_file_path = self.file_helpers.get_metadata_file_path()
        metadata = self.file_helpers.get_file_content(metadata_file_path)

        # parse the metadat into a json dict 
        self.metadata = json.loads(metadata)

    def detect_files(self):
        query = FILE_DETECTION_HUMAN_PROMPT.format(input=self.user_query, metadata=self.metadata)
        response = self.chain.invoke({"input": query})
        content = response.content
        return content


        