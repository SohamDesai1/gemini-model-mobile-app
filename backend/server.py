from flask import Flask, request,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/data')
def main():
    return {"message": 'Hello World'}

if __name__ == "__main__":
    app.run(debug=True)