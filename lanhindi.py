import pyttsx3
import speech_recognition as sr
from googletrans import Translator


engine = pyttsx3.init()
voices = engine.getProperty('voices')

def say(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

def translate_hindi_to_english(hindi_text):
                translator = Translator()
                print("Translating...")
                # Translate from Hindi to English
                translation = translator.translate(hindi_text, src='hi', dest='en')
                # print(translation)
                # Return the translated text
                return (translation.text)


if __name__ == "__main__":

    speak("नमस्ते")
    with sr.Microphone() as source:
        # speak("नमस्ते आप क्या")
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language="hi-in")
            speak(command)
            # Example usage
            # hindi_text = "यह हिंदी टेक्स्ट को अंग्रेजी में अनुवाद करें"
            english_text = translate_hindi_to_english(command)
            say(english_text)
            print(english_text)

        except Exception as e:
            print(e)
