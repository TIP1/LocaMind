# 🖥️ CLI (ui/cli.py):
import time
import typer
from agent.llm_interface import ModelInterface

app = typer.Typer()

@app.command()
def chat():

    llm_model = ModelInterface(model_name="mixtral", url="http://localhost:11434/api/generate")

    while True:
        prompt = input(">>> ")
        if prompt.lower() in ["exit", "quit"]:
            break
        response = llm_model.query_model(prompt)
        print("AI:", response)

