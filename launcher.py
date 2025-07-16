import subprocess
import webbrowser
import time

MODEL_NAME = "tinyllama"

def check_ollama():
    try:
        subprocess.run(["ollama", "version"], check=True, stdout=subprocess.DEVNULL)
        return True
    except:
        return False

def check_model():
    result = subprocess.run(["ollama", "list"], stdout=subprocess.PIPE)
    return MODEL_NAME in result.stdout.decode()

# Check for Ollama installation
if not check_ollama():
    print("Ollama is not installed. Opening download page...")
    webbrowser.open("https://ollama.com/download")
    exit()

# Check for tinyllama model
if not check_model():
    print(f"{MODEL_NAME} model not found. Downloading now...")
    subprocess.run(["ollama", "pull", MODEL_NAME])

# Launch the Streamlit app
print("Launching Homework Helper...")
subprocess.Popen(["streamlit", "run", "app.py"])
time.sleep(3)
webbrowser.open("http://localhost:8501")
