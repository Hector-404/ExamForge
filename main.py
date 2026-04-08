from fastapi import FastAPI

app = FastAPI()

def clean_notes(notes):
    return notes.strip()
def explain_notes(notes):
    return "Explanation: " + notes
def format_answer(notes):
    return "Exam Answer: " + notes

@app.get("/")
def home():
    return {"message": "ExamForge is running"}

@app.post("/process-notes")
def process_notes(data: dict):
    notes = data.get("notes", "")

    cleaned = clean_notes(notes)
    explanation = explain_notes(cleaned)
    answer = format_answer(cleaned)

    return {
        "cleaned_notes": cleaned,
        "explanation": explanation,
        "exam_answer": answer
    }