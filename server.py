from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    statement = request.args.get('textToAnalyze')  # Cambiado de form a args para GET
    result = emotion_detector(statement)
    
    if 'error' in result:
        response_text = f"Error processing the statement: {result['error']}"
    else:
        response_text = f"For the given statement, the system response is: "
        for emotion, score in result.items():
            if emotion != 'emociones_dominantes':
                # Convertir score a float antes de formatearlo
                formatted_score = float(score)
                response_text += f"'{emotion}': {formatted_score:.9f}, "
        
        response_text = response_text.rstrip(', ')
        
        dominant_emotion = result['emociones_dominantes']
        response_text += f". The dominant emotion is {dominant_emotion}."
    
    return render_template('index.html', response=response_text)

if __name__ == '__main__':
    app.run(debug=True, port=5000)