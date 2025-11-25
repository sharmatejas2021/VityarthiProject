# app.py
# simple, friendly Flask backend that processes resumes in memory

from flask import Flask, request, jsonify
from parser import extract_text_from_fileobj
from scoring import evaluate_resume

app = Flask(__name__)

@app.route("/evaluate", methods=["POST"])
def evaluate():
    file = request.files.get("resume")
    if not file:
        return jsonify({"error": "No file uploaded. Please pick a file."}), 400

    text = extract_text_from_fileobj(file, file.filename)
    result = evaluate_resume(text)
    return jsonify(result)

@app.route("/health")
def health():
    return {"status": "running"}

if __name__ == "__main__":
    app.run(debug=True)
