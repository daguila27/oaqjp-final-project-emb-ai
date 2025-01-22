import requests
import json

def emotion_detector(text_to_analyze):
    if text_to_analyze == "":  
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
    }
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, headers=headers, json=input_json)
    response_data = response.json()
    emotionPredictions = response_data.get("emotionPredictions")
        
    emotion_scores = {
        "anger": 0,
        "disgust": 0,
        "fear": 0,
        "joy": 0,
        "sadness": 0
    }
    emotion_id = "anger"
    for emotion in emotionPredictions:
        for emotion_id in emotion_scores:
            emotion_scores[emotion_id] = emotion.get('emotion').get(emotion_id)
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        emotion_scores["dominant_emotion"] = dominant_emotion

    return emotion_scores