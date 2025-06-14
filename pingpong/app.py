from flask import Flask, jsonify

app = Flask(__name__)
counter = 0

@app.route('/ping')
def ping():
    global counter
    counter += 1
    return "Pong!"

@app.route('/count')
def count():
    return jsonify({"count": counter})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
