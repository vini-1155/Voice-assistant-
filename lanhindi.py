import pyttsx3
import openai
from openai import OpenAI
import speech_recognition as sr

key_value = os.environ.get('KEY')

def ai(userquery):
    try:
        client = OpenAI(
            api_key=key_value)
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
