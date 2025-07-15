# 🧠 AI Text Summarizer Web App

A simple yet powerful Flask-based web app that uses a Transformer model to summarize long text into short, meaningful summaries. Built using HuggingFace Transformers and designed for real-world use cases.

---

## 🌐 Live Demo

> 📸 — images/image.png

---

## 🚀 Features

* Paste or type long text and get short, concise summaries
* Built using `distilbart-cnn-12-6` model from HuggingFace
* Lightweight, fast, and production-ready
* Clean Flask-based frontend with Bootstrap styling

---

## 🧩 Tech Stack

* **Frontend:** HTML + CSS (Bootstrap)
* **Backend:** Flask
* **AI Model:** `sshleifer/distilbart-cnn-12-6`
* **Libraries:** HuggingFace Transformers

---

## 📁 Folder Structure

```
ai_summarizer_app/
├── static/               # CSS styling (optional)
├── templates/
│   └── index.html        # Frontend page
├── summarizer.py         # Summarization logic
├── app.py                # Flask application
└── images/
    └── image.png         # Screenshot of the UI
```

---

## ⚙️ Setup Instructions

1. **Clone the repo:**

```bash
git clone https://github.com/SyedSafeerHussain/ai-text-summarizer-webapp.git
cd ai-text-summarizer-webapp
```

2. **Create virtual environment & activate:**

```bash
python -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the app:**

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📝 How It Works

* User enters/pastes any long-form text
* Flask sends the text to the `summarizer.py` pipeline
* HuggingFace Transformer generates a summary
* The summary is displayed on the same page

---

## 📦 Example Input

> *"Climate change is a long-term shift in temperatures and weather patterns. These changes may be natural..."*

### 🧾 Output

> *"Climate change refers to long-term changes in temperature and weather patterns. These shifts are often caused by human activity..."*

---

## 🤖 Model Info

* **Model:** `sshleifer/distilbart-cnn-12-6`
* **Type:** Encoder-decoder (Transformer)
* **Task:** Text Summarization
* **Source:** HuggingFace 🤗

---

## ✨ Future Upgrades

* Larger model support (`bart-large-cnn`)
* Language detection
* Summary download as PDF
* REST API for external usage

---

## 👨‍💻 Author

**Safeer Hussain**
AI-Powered Developer | Automation Enthusiast
[GitHub Profile](https://github.com/SyedSafeerHussain)

## 📜 License

MIT License — feel free to use and modify.

---

> "Smart code. Real results. Minimal effort."
