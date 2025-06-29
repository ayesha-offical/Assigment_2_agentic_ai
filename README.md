# 🧠 AI Code Assistant / Dawai Info Agent

This Python project uses a Gemini-powered LLM (via OpenAI-compatible API) to respond to user input. You can configure it to act as either:

- 💊 **Dawai Information Agent** — answers healthcare-related questions.
- 👨‍💻 **Code Helper Agent** — answers programming-related questions and politely declines unrelated topics.

---

## 📁 Project Structure

```
ai_agent_assistant/
├── main.py
├── .env
├── README.md
└── agents/
    ├── __init__.py
    ├── agent.py
    ├── runner.py
    └── models.py
```

---

## ⚙️ Setup Instructions

### 1. Install Required Package

```bash
pip install python-dotenv
```

### 2. Create `.env` File

Add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## 🚀 How to Run

Run the app using:

```bash
python main.py
```

You'll be asked:

```
Please enter your question:
```

And you'll get a response from the agent.

---

## 🤖 Agent Modes

Update the agent block in `main.py` to switch roles:

### 🩺 Dawai Information Agent

For Dawai-related questions:

```
You are a helpful assistant that provides information about Dawai, a healthcare platform. Answer questions based on the provided context.
```

### 💻 Code Helper Agent

For programming questions only:

```
You are a helpful coding assistant. Answer the user's questions about programming and provide code examples when necessary. When someone asks about anything other than code or programming, say you can't give information on that.
```

---

## 📝 Notes

Ensure your `agents/` folder contains the following:

- `Agent`
- `Runner`
- `AsyncOpenAI`
- `OpenAIChatCompletionsModel`

---

Made with ❤️ by Ayesha
