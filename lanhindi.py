import pyttsx3
import speech_recognition as sr
from googletrans import Translator


engine = pyttsx3.init()
voices = engine.getProperty('voices')


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()


t = Translator()
r = sr.Recognizer()


if __name__ == "__main__":
    speak("नमस्ते")
    with sr.Microphone() as source:
        # speak("नमस्ते आप क्या")
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language="hi-in")
            speak(command)
            translator = Translator()
            translation = translator.translate(command, dest='en')
            print(translation.text)
        except Exception as e:
            print(e)
