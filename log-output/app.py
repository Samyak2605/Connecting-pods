import uuid
from datetime import datetime
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    timestamp = datetime.utcnow().isoformat() + "Z"
    unique_id = str(uuid.uuid4())
    
    try:
        res = requests.get("http://pingpong-service/count")
        count = res.json().get("count", "?")
    except:
        count = "?"

    return f"{timestamp}: {unique_id}.\nPing / Pongs: {count}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
