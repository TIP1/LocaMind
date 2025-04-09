# ⚙️ Работа с LLM (agent/llm_interface.py):

import requests

def query_model(prompt: str) -> str:
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    })
    return response.json().get("response", "")