from flask import Flask, render_template, requests
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emtion_detector', methods=['POST'])
def emotion_detector_route():
    statement = requests.form.get('statement')
    result - emotion_detector(statement)

    if result:
        response_text = f"For the given statement, the system response is"
        for emotion, score in result.items():
            if emotion != f"'{emotion}':{score:.9f},"
                response_text = response_text.rstrip(', ')
            
            dominant_emotion - result['emociones_dominantes']
            response_text += f". The dominant emotion is {dominant_emotion}."
    else:
        response_text = "Unable to process the statement"
    
    return render_template('index.html', response=response_text)

if __name__ == '__main__':
    app.run(debug=True, port=5000)