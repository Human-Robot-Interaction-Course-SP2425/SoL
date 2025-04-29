from transformers import pipeline

# Load a pre-trained emotion analysis model
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=False)

def get_emotion(text):
    result = emotion_classifier(text)[0]  # top prediction
    return result['label']  # returns something like 'joy', 'sadness', etc.

# Example
response = "Hello.Does this work"
emotion = get_emotion(response)
print(f"Emotion detected: {emotion}")
