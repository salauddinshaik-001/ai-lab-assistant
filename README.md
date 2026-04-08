# 🤖 AI Lab Assistant

An intelligent AI-powered assistant built using **LangChain** and **Groq LLMs** to help students with Computer Science subjects.

---

## 🚀 Features

* 💬 Interactive chatbot interface using Streamlit
* 🧠 Context-aware responses with memory
* ⚡ Fast responses using Groq LLM API
* 📚 Helps with Computer Science queries
* 🖥️ Simple and user-friendly UI

---

## 🛠️ Technologies Used

* Python
* Streamlit
* LangChain
* Groq API (LLMs)
* dotenv (for environment variables)

---

## 📂 Project Structure

```
ai-lab-assistant/
│── app.py              # Streamlit frontend
│── assistant.py        # AI logic & LLM integration
│── requirements.txt    # Dependencies
│── .gitignore          # Ignored files
│── README.md           # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/salauddinshaik-001/ai-lab-assistant.git
cd ai-lab-assistant
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add API Key

Create a `.env` file and add:

```
GROQ_API_KEY=your_api_key_here
```

---

### 5. Run the app

```bash
streamlit run app.py
```

---

## 📸 Output

The application provides an interactive chatbot interface where users can ask questions related to Computer Science topics and receive intelligent responses.

---

## 🔐 Security Note

API keys are stored securely using environment variables and are excluded from version control using `.gitignore`.

---

## 🎯 Future Improvements

* Add voice input/output
* Improve UI design
* Add more AI models
* Deploy application online

---

## 👨‍💻 Author

**Salauddin Shaik**
Computer Science Engineering (AI & ML)

---

## ⭐ Conclusion

This project demonstrates the integration of **LLMs with real-world applications** using LangChain and Groq, providing an efficient AI assistant for students.
