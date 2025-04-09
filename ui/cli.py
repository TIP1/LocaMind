# 🖥️ CLI (ui/cli.py):

import typer
from agent.llm_interface import query_model

app = typer.Typer()

@app.command()
def chat():
    while True:
        prompt = input(">>> ")
        if prompt.lower() in ["exit", "quit"]:
            break
        response = query_model(prompt)
        print("AI:", response)

