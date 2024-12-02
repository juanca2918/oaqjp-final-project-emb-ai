import requests

def emotion_detector(variable):
    text_to_analyze = variable.strip()

    if not text_to_analyze:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "emociones_dominantes": None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, headers=headers, json=input_json)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "emociones_dominantes": None
            }
        else:
            return {
                "error": f"HTTP error occurred: {http_err}",
                "status_code": response.status_code
            }
    except requests.exceptions.RequestException as err:
        return {
            "error": f"Request failed: {err}"
        }

    if response.status_code == 200:
        response_data = response.json()
        emociones = response_data['emotionPredictions'][0]['emotion']
        formato_saliente = {
            "anger": emociones.get("anger", 0),
            "disgust": emociones.get("disgust", 0),
            "fear": emociones.get("fear", 0),
            "joy": emociones.get("joy", 0),
            "sadness": emociones.get("sadness", 0)
        }
        emociones_dominantes = max(formato_saliente, key=formato_saliente.get)
        formato_saliente['emociones_dominantes'] = emociones_dominantes
        return formato_saliente
    else:
        return {
            "error": "Failed to get a response",
            "status_code": response.status_code
        }
