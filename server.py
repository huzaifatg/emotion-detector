from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def analyze():
    text = request.args.get('textToAnalyze')

    if text is None or text == "":
        return "Invalid input! Please try again."

    result = emotion_detector(text)

    return str(result)

if __name__ == "__main__":
    app.run(debug=True)