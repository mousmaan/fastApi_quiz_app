import json
import random
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("questions.txt") as f:
    questions = json.load(f)

@app.get("/")
def root():
    return FileResponse("index.html")

@app.get("/random_question")
def get_random_question():
    q_index = random.randint(0, len(questions) - 1)
    q = questions[q_index].copy()
    q["index"] = q_index
    return q

@app.get("/check_answer/{q_index}/{selected}")
def check_answer(q_index: int, selected: str):
    correct = questions[q_index]["answer"]
    return {"correct": correct, "is_correct": (selected.upper() == correct)}

@app.get("/show_brief/{q_index}")
def show_brief(q_index: int):
    return {"brief": questions[q_index]["brief"]}

@app.get("/show_detailed/{q_index}")
def show_detailed(q_index: int):
    return {"detailed": questions[q_index]["detailed"]}
