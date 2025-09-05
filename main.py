import json
import random
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()

with open("questions.txt") as f:
    questions = json.load(f)

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.get("/random_question")
def random_question():
    q = random.choice(questions)
    q_copy = q.copy()
    q_copy.pop("answer")
    q_copy.pop("brief")
    q_copy.pop("detailed")
    return q_copy

@app.get("/show_brief/{q_index}")
def show_brief(q_index: int):
    return {"brief": questions[q_index]["brief"]}

@app.get("/show_detailed/{q_index}")
def show_detailed(q_index: int):
    return {"detailed": questions[q_index]["detailed"]}
