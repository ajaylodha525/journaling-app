from flask import Flask, render_template, request, redirect
from textblob import TextBlob
import json
import os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = "entries.json"

def load_entries():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_entries(entries):
    with open(DATA_FILE, "w") as f:
        json.dump(entries, f, indent=2)

def get_mood(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

@app.route("/", methods=["GET", "POST"])
def index():
    entries = load_entries()
    if request.method == "POST":
        text = request.form.get("entry")
        if text:
            mood = get_mood(text)
            entries.insert(0, {
                "text": text,
                "mood": mood,
                "date": datetime.now().strftime("%d %b %Y, %I:%M %p")
            })
            save_entries(entries)
        return redirect("/")
    return render_template("index.html", entries=entries)

if __name__ == "__main__":
    app.run(debug=True)