import speech_recognition as sr
import os
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# print(voices[1].id)

'''
def speak(audio):
speak("Hello Vinay!!")
'''


def say(text):
    engine.say(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print("User said:", query)
            say(query)
            return query
        except Exception as e:
            return "Can You try saying once again!!"


if __name__ == '__main__':
    # say("Hello I am Guna how can I help You")
    while True:
        print("Listening...")
        text = takecommand()
