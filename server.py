from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emote_detector():
    """ 
    GET the response based on the user text input
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger, disgust, fear, joy, sadness = (
    response['anger'],
    response['disgust'],
    response['fear'],
    response['joy'],
    response['sadness']
)

    dominant_emotion = response['dominant_emotion']
    response = (
    f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
    f"'sadness': {sadness}. "
    f"The dominant emotion is {dominant_emotion}."
)


    if dominant_emotion is None:
        return "Invalid text! Please try again!."
    return response

@app.route("/")
def render_index_page():
    """
    Intialize the home page of the interface with index.html template
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
    