This project involves building a question/explanation web app with Python (FastAPI) and a simple HTML frontend, using data stored as JSON in a TXT file.
Ye project 3 cheezon se milke bana hai:

Data (TXT as JSON):
Aapke MCQ questions ko proper JSON format me save kiya gaya hai, jisme question, options, correct_answer, brief_explanation (~4 lines), detailed_explanation (~20 lines) included hain.

FastAPI Backend (Python):
Ek chhota API server banaya hai jo /api/random-question endpoint se random question deta hai (saath me options, correct answer, brief & detailed explanations). Root “/” pe index.html serve hota hai.

HTML Frontend:
Simple page jisme buttons hain:

New Question – random question laata hai

Submit – aapke select kiye option ko check karta hai

Show Solution (Brief) – 4-line wali explanation dikhata hai

Show Detailed Explanation – ~20 line wali deep explanation dikhata hai

Files & Structure

Aapke project folder me bas 3 files honge:

aero-mcq/
├── app.py                 # FastAPI backend
├── index.html             # Frontend UI
└── questions_data.txt     # JSON data (TXT file)


Bas itna hi chahiye start karne ke liye. Later, agar aap chahe to static folder, tests, etc. add kar sakte ho.

Dependencies (Mac + VS Code)

Python 3.10+ (Mac pe usually preinstalled hota hai; 3.11 preferred)

FastAPI (backend framework)

Uvicorn (ASGI server)


Project Overview
You’ll:

Convert a document with questions and answers into a JSON TXT file (with added explanations).

Write a Python FastAPI backend that reads this TXT, returns a random question, and exposes solutions via endpoints.

Make a basic HTML page to show questions, options, and explanations, connecting it to the FastAPI backend.

Run and test everything on your Mac with VS Code.

Files to Create and Their Locations
You’ll create only three main files inside your project folder (e.g., quiz-app):

questions.txt: Contains the questions, options, answers, and all explanations in JSON format.

main.py: Your FastAPI Python backend.

index.html: The frontend HTML for user interaction.

Create the folder anywhere (e.g., in Documents), open in VS Code, and keep all three files in the same folder.

Dependencies Needed
Python 3 (should be installed—verify in terminal: python3 --version)

FastAPI (backend framework)

Uvicorn (for running your API server)

Jinja2 (for serving HTML templates, optional since simple HTML can be static)

Install dependencies in VS Code terminal by running:

text
pip install "fastapi[standard]"
pip install uvicorn
