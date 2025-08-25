import asyncio
import speech_recognition as sr
import pyttsx3
from googletrans import Translator

r = sr.Recognizer()

def record_speech():
    """ Listens for audio input and converts it to a string. """

    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2)

        while True:
            audio = r.listen(source2)
            try:
                text = r.recognize_google(audio, language="el-GR")
                print(f"User: {text}")
                return text
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Request error; {0}".format(e))

async def translate_speech(text,src_language="el",dest_language="en"):
    """ Sends speech to google translate for translation. """
    translator = Translator()
    translation = await translator.translate(text,src=src_language,dest=dest_language)
    print(f"AI: {translation.text}")
    return translation.text

def speak_translated_text(command):
    """ Plays translated speech as audio. """
    engine = pyttsx3.init()
    engine.setProperty("voice","com.apple.speech.synthesis.voice.eloquence.en-US.Read")
    engine.say(command)
    engine.runAndWait()
    return

while True:
    speech = record_speech()
    translated_speech = asyncio.run(translate_speech(speech))
    speak_translated_text(translated_speech)