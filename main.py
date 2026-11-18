import time
import threading
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

def write_logs():
    while True:
        with open("/logs/app.log", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%H:%M:%S')}] Service is running smoothly!\n")
        time.sleep(5)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Kubernetes Pod!", "status": "ok"})

if __name__ == '__main__':
    threading.Thread(target=write_logs, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)
