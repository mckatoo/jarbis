import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        audio = recognizer.listen(source)
        print(recognizer.recognizer_sphinx(audio))
