from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load a small local text-generation model
generator = pipeline("text-generation", model="gpt2")

@app.route("/", methods=["GET", "POST"])
def home():
    meditation_text = ""
    if request.method == "POST":
        name = request.form.get("name")
        mood = request.form.get("mood")

        prompt = f"Write a short personalized prayer/meditation for {name}, who is feeling {mood}."

        response = generator(prompt, max_length=80, num_return_sequences=1)
        meditation_text = response[0]["generated_text"]

    return render_template("index.html", meditation_text=meditation_text)

if __name__ == "__main__":
    app.run(debug=True)
