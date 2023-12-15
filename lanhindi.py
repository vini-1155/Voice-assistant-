import pyttsx3
import openai
# from config import apikey
from openai import OpenAI
import speech_recognition as sr
from googletrans import Translator
from deep_translator import GoogleTranslator

engine = pyttsx3.init()
voices = engine.getProperty('voices')

def say(text):
    engine.setProperty('voice', voices[3].id)
    engine.say(text)
    engine.runAndWait()

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 180)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

def ai(userquery):
    try:
        client = OpenAI(
            api_key="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")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {
                    "role": "user",
                    "content": userquery
                }
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # print(response.choices)
        generated_texts = [
            choice.message.content for choice in response.choices
        ]

        # say(''.join(generated_texts))
        # print(''.join(generated_texts))
        trans_hindi_to_eng(''.join(generated_texts))



    except Exception as e:
        print(e)
def trans_hindi_to_eng(eng):
    trans = GoogleTranslator(source="english", target="hindi").translate(eng)
    speak(trans)   

def translate_hindi_to_english(hindi_text):
                trans = GoogleTranslator(source="hindi", target="english").translate(hindi_text)
                return trans
     

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
            ai(english_text)

        except Exception as e:
            print(e)
