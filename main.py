import speech_recognition as sr
import pyaudio as pya
r= sr.Recognizer()
with sr.Microphone() as source:
    print("Ses dinleniyor.")
    audio=r.record(source,duration=3.5)
    try:
        str=r.recognize_google(audio,language="tr-tr")
        print(str)
    except:
        print("Hata oluştu.")
