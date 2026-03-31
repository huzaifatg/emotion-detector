# Emotion Detector

This project is an AI-based web application that detects emotions from user input text using the IBM Watson NLP library.

## 📌 Features
- Detects emotions from text
- Returns anger, disgust, fear, joy, and sadness scores
- Identifies dominant emotion
- Web interface using Flask
- Includes error handling and unit testing

## ⚙️ Technologies Used
- Python
- Flask
- IBM Watson NLP
- Requests library

## 🚀 How to Run

1. Clone the repository:
   git clone https://github.com/<your-username>/emotion-detector

2. Navigate to the project directory:
   cd emotion-detector

3. Run the server:
   python server.py

4. Open in browser:
   http://127.0.0.1:5000/emotionDetector?textToAnalyze=I am happy

## 🧪 Testing
Run unit tests using:
python test_emotion_detection.py

## 📊 Output Example
{
  "anger": 0.01,
  "disgust": 0.0,
  "fear": 0.0,
  "joy": 0.95,
  "sadness": 0.02,
  "dominant_emotion": "joy"
}

## 📁 Project Structure
- emotion_detection.py
- server.py
- test_emotion_detection.py
- README.md