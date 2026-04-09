# 🚀 ExamForge

An AI-powered backend system that transforms raw student notes into **clean, structured, and exam-ready answers**.

---

## 🧠 What This Project Does

ExamForge takes unstructured notes and:
- Cleans them  
- Explains them in simple terms  
- Converts them into exam-ready answers  

---

## ✨ Features

- 🧹 Note cleaning  
- 📘 Explanation generation  
- 📝 Exam answer formatting  
- ⚙️ Built with FastAPI  

---

## 🛠️ Tech Stack

- Python  
- FastAPI  
- Uvicorn  

---

## 📡 API Endpoints

### 🔹 GET `/`
Check if server is running  

---

### 🔹 POST `/process-notes`

#### Request:
```json
{
  "notes": "AI is a field of computer science",
  "level": "easy"
}
```

#### Response:
```json
{
  "cleaned_notes": "AI is a field of computer science",
  "explanation": "Explanation: AI is a field of computer science",
  "exam_answer": "Exam Answer: AI is a field of computer science"
}
```

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/Hector-404/ExamForge.git
cd ExamForge
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
uvicorn main:app --reload
```

---

## 📈 Future Improvements

- 🤖 Add real AI integration (OpenAI / LLMs)  
- 🎯 Difficulty-based explanations (easy/medium/hard)  
- 🌐 Add frontend UI  
- ☁️ Deploy backend  

---

## 👨‍💻 Author

Mohammad Hammad Khan
