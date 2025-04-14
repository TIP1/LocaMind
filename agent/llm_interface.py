# ⚙️ Работа с LLM (agent/llm_interface.py):

import requests



class ModelInterface:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            return cls._instance

    def __init__(self, model_name, url):
        self.model_name = model_name
        self.url = url

        self.query_model(
            f"My name is Tip. Text with me on russian language. Write responsec in json format. If you have a code, it must be in dictinary format where key is name of file with extension and content is value ")

    def query_model(self, prompt: str) -> str:
        print(f"Prompt: {prompt}")
        response = requests.post(self.url, json={
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
        })
        answer = response.json().get("response", "")
        print(f"Answer: {answer}")
        return answer