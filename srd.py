import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source,phrase_time_limit = 3)
try:
    text = r.recognize_google(audio)
    print(text)
except sr.RequestError as e:
    print("Error!")
