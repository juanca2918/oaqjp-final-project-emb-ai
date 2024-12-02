from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    statement = request.args.get('textToAnalyze')

    # Llamamos al detector de emociones
    result = emotion_detector(statement)
    
    if 'error' in result:
        # Manejo del error recibido desde el detector de emociones
        response_text = f"Error: {result['error']}"
        if 'status_code' in result:
            response_text += f" (Status Code: {result['status_code']})"
    elif all(value is None for value in result.values()):
        # Manejo del caso donde todas las emociones son None
        response_text = "Invalid text! Please try again!"
    else:
        # Construcción de la respuesta exitosa
        response_text = f"For the given statement, the system response is: "
        for emotion, score in result.items():
            if emotion != 'emociones_dominantes' and score is not None:
                formatted_score = float(score)
                response_text += f"'{emotion}': {formatted_score:.9f}, "

        response_text = response_text.rstrip(', ')

        dominant_emotion = result['emociones_dominantes']
        if dominant_emotion:
            response_text += f". The dominant emotion is {dominant_emotion}."
        else:
            response_text += ". Unable to determine the dominant emotion."

    return render_template('index.html', response=response_text)

if __name__ == '__main__':
    app.run(debug=True, port=5000)