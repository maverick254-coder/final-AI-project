# 📚 Homework Helper – Offline AI-Powered Homework Assistant

> Final Project – AI for Software Engineering  
> Built with Streamlit + Ollama + TinyLLaMA  
> SDG-Focused: Quality Education (SDG 4) & Infrastructure (SDG 9)

---

## 🎯 SDG Goals
- **SDG 4 – Quality Education**: Enables students to get offline AI help with homework.
- **SDG 9 – Innovation & Infrastructure**: Leverages lightweight, locally deployed AI.

---

## 🚀 Features
- Works fully offline after setup
- Uses TinyLLaMA or LLaMA 3 via Ollama for fast inference
- Built with Streamlit, packaged as a desktop app
- One-click installer with helper script

---

## 🖥 How to Run (Developer Mode)

# 1. Set up virtual environment
python -m venv venv
venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Ensure Ollama is installed and running
ollama run tinyllama

# 4. Launch app
streamlit run app.py


## 🔽 Download the App(user mode)

To get started without code:

👉 [Download the Installer (.exe)](https://github.com/your-username/your-repo/releases)

> ⚠️ Note: `OllamaSetup.exe` is not included in this GitHub repo, but is bundled inside the installer and will run automatically. No manual installation is needed.

---

## 💡 What If I Clone This Repo Instead?

If you are cloning this repo (e.g., for development), make sure you:
1. Install [Ollama manually](https://ollama.com/download)
2. Run:
   
   ollama run tinyllama
   streamlit run app.py


