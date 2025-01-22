"""
Este módulo define una aplicación web Flask para la detección de emociones.
La aplicación acepta la entrada de texto del usuario y devuelve las emociones detectadas.
"""
from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector
app = Flask(__name__)
@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    Detecta la emoción dominante de un texto dado.

    Retorna:
        Respuesta JSON con las emociones detectadas y sus puntuaciones,
            o un mensaje de error por entrada no válida.
    """

    # Obtiene el texto enviado en la solicitud
    text_to_analyze = request.args.get("textToAnalyze")

    # Ejecuta la función emotion_detector
    result = emotion_detector(text_to_analyze)

    ## Retorna 400 si dominant_emotion es None
    if result['dominant_emotion'] is None:
        return jsonify("Invalid text! Please try again!.")

    # Crea el mensaje de salida
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return jsonify(response_text)

@app.route('/')
def home():
    """
    Renderiza el formulario plantilla para la aplicación.
    """
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, port=5000)
