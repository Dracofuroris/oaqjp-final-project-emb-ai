"""
Crear una aplicación de detección de emociones utilizando
la biblioteca Watson NLP
"""
#Importa libreria json
import json
#Importa libreria requests
import requests

def emotion_detector(text_to_analyze):
    """
    Función para acceder a la biblioteca Watson NLP a través
    de una solicitud POST y almacenar la respuesta en una variable
    que se retornanará como un ".text"
    """
    #Datos de la biblioteca Watson NLP
    url = 'https://sn-watson-emotion.labs.skills.network' \
          '/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyze } }

    #Almacenamiento de la respuesta 
    response = requests.post(url, json = my_obj, headers=header, timeout=3.00)

    #Formateo de la respuesta
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        #Ruta del diccionario donde se encuentran los valores de todas las emociones
        path = formatted_response["emotionPredictions"][0]["emotion"]
        
        #Extraer valores de las emociones
        anger_score = path["anger"]
        disgust_score = path["disgust"]
        fear_score = path["fear"]
        joy_score = path["joy"]
        sadness_score = path["sadness"]

        #Lista vacia
        scores = []
        
        #Añadir los valores de las emociones a la lista "scores"
        for key in path:
            scores.append(path[key])

        #Busca el valor maximo de la lista
        score_dominant_emotion = max(scores)

        #Busca la emocion con el valor mas alto y lo asigna a la variable "dominant_emotion"
        for key in path:
            if path[key] == score_dominant_emotion:
                dominant_emotion = key
    elif response.status_code == 400:
        #Todos los valores para todas las claves del diccionario son None
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
    
    #Regresa un diccionario con los valores de cada emoción y la emoción dominante
    return {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion
    }
    