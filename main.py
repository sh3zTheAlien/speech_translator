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
                print(text)
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Request error; {0}".format(e))

def translate_speech(text):
    """ Sends speech to google translate for translation. """
    pass

def speak_translated_text(command):
    """ Plays translated speech as audio. """
    pass

record_speech()