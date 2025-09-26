import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

API_KEY = "AIzaSyBwSCBSo7OjXtdda4j4BHmtLxfV9cFyK_4"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Dinliyorum...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="tr-TR")
            print(f"Kullanıcı: {text}")
            return text
        except sr.UnknownValueError:
            print("Söylediğini anlayamadım.")
            return ""
        except sr.RequestError:
            print("Servise ulaşılamadı.")
            return ""

while True:
    user_input = listen()
    if user_input:
        response = model.generate_content(user_input)
        print("Asistan:", response.text)
        speak(response.text)



