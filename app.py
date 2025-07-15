from flask import Flask, render_template, request
from summarizer import generate_summary

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        input_text = request.form.get("input_text")
        if input_text:
            summary = generate_summary(input_text)
    return render_template("index.html", summary=summary)
if __name__=="__main__":
    app.run(debug=True)