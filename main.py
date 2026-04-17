from fastapi import FastAPI

app = FastAPI()

def clean_notes(notes):
    return notes.strip()
def explain_notes(notes, level):
    explanations = {
        "easy" : "Simple Explanation : ",
        "medium" : "Detailed Explanation : ",
        "hard" : "Advanced Explanation :"
    }
    prefix = explanations.get(level, explanations["easy"])
    return prefix + notes
def format_answer(notes):
    return "Exam Answer: " + notes

@app.get("/")
def home():
    return {"message": "ExamForge is running"}

@app.post("/process-notes")
def process_notes(data: dict):
    notes = data.get("notes", "")
    level = data.get("level", "easy").lower().strip()

    cleaned = clean_notes(notes)
    explanation = explain_notes(cleaned,level)
    answer = format_answer(cleaned)

    return {
        "cleaned_notes": cleaned,
        "explanation": explanation,
        "exam_answer": answer
    }