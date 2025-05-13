''' 
Ejecutar la funcion inicializa la aplicación de detección de emociones 
para ser ejecutado a través del canal Flask y desplegado en
localhost:5000.
'''
# Importa Flask, render_template, request del paquete flask
from flask import Flask, render_template, request
# Importa la función emotion_detector del paquete creado
from EmotionDetection.emotion_detection import emotion_detector

#Inicializa flask
app = Flask(__name__)

@app.route("/emotionDetector")
def sent_detector():
    """
    Este código recibe el texto de la interfaz HTML y ejecuta una detección 
    de emociones mediante la función emotion_detector. El resultado muestra 
    los valores de cada emoción y cual de estas es la más dominante.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    #Si la condicion es verdadera significa que hubo un status_code igual a 400
    if response["dominant_emotion"] is None:
        return "¡Texto inválido! ¡Por favor, inténtalo de nuevo!"

    #Regresa la salida solicitada en el laboratorio
    return f"Para la declaración dada, la respuesta del sistema es " \
           f"anger: {response['anger']}, disgust: {response['disgust']} " \
           f"fear: {response['fear']}, joy: {response['joy']} " \
           f"sadness: {response['sadness']}. " \
           f"La emoción dominante es {response['dominant_emotion']}"

@app.route("/")
def render_index_page():
    ''' 
    Esta función inicia la renderización de la página principal de la 
    aplicación a través del canal Flask.
    '''
    return render_template("index.html")

if __name__ == "__main__":
    #Esta función ejecuta la aplicación Flask y la implementa en localhost:5000
    app.run(host="0.0.0.0", port=5000)
