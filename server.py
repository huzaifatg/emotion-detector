from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return "Emotion Detector App"

@app.route("/emotionDetector")
def analyze():
    text = request.args.get('textToAnalyze')

    if text is None or text == "":
        return "Invalid input! Please try again."

    result = emotion_detector(text)

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(debug=True)