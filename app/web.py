from flask import Flask, render_template, request
from app.services.analyzer_service import analyze
import os

# 🔥 Fix template path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        password = request.form.get("password")
        result = analyze(password).to_dict()

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
