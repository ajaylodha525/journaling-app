# Journaling App

A small journaling web app I built with Flask. You write an entry, and the app tags it as Positive, Neutral or Negative based on the sentiment of the text.

I made it to get hands-on with a basic NLP task in Python, and to practice building a complete Flask app with a form, templates and simple file storage.

## How it works

Each entry is analysed with TextBlob, which scores the text between -1 (very negative) and +1 (very positive). A score above 0.1 is tagged Positive, below -0.1 is Negative, and anything in between is Neutral. Entries are saved with a timestamp in a local `entries.json` file and shown newest first.

TextBlob is a lexicon-based tool. It looks up word polarities in a fixed dictionary and averages them, so it is not a trained deep learning model. That also means it works better on full sentences than on single words. A lone word like "stress" comes out Neutral, while "I am very stressed and anxious today" is picked up as Negative.

## Built with

- Python
- Flask
- TextBlob
- HTML and CSS (Jinja templates)

## Running it locally

```bash
git clone https://github.com/ajaylodha525/journaling-app.git
cd journaling-app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m textblob.download_corpora
python app.py
```

Then open `http://127.0.0.1:5000` in your browser. On macOS or Linux, activate the environment with `source venv/bin/activate` instead.

## Things I want to improve

- Try a pre-trained transformer model for sentiment and compare it with TextBlob
- Add a mood-over-time chart
- Let entries be edited and deleted

## Author

Ajay Lodha, B.Tech Computer Science student learning data science.
