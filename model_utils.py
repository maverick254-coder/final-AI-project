import subprocess

def ask_ollama(prompt, model="tinyllama"):
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60  # seconds
        )
        return result.stdout.decode("utf-8")
    except subprocess.TimeoutExpired:
        return "The model took too long to respond."
    except Exception as e:
        return f"Error: {str(e)}"
