import pyttsx3
import openai
from openai import OpenAI
import speech_recognition as sr

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
        res = ''.join(generated_texts)
        print("ai",res)
        return res

    except Exception as e:
        print(e) 

# if __name__ == "__main__":
#     speak("नमस्ते")
#     with sr.Microphone() as source:
#         # speak("नमस्ते आप क्या")
#         print("Listening...")
#         audio = r.listen(source)
#         try:
#             command = r.recognize_google(audio, language="hi-in")
#             speak(command)

#         except Exception as e:
#             print(e)
