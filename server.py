"""
Module Name: server.py

This module handles requested from clients.

Author: Sevak
Date: 24/08/24
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    /emotionDetector route handler
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if not response['dominant_emotion']:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is"
        f"'anger': {anger}, 'disgust':{disgust}, 'fear': {fear}, 'joy'"
        f": {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    root route handler
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010)
