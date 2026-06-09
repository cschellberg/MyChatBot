from configparser import ConfigParser
from pathlib import Path

class Config:
    def __init__(self,config_file="~/IdeaProjects/MyChatBot/src/langgraphagenticai/ui/uiconfigfile.ini"):
        expanded_path = Path(config_file).expanduser()
        if not expanded_path.exists():
            raise FileNotFoundError(f"Config file not found: {config_file}")
        self.config = ConfigParser()
        self.config.read(str(expanded_path))

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(",")

    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(",")

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(",")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")