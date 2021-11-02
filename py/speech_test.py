import speech_recognition as sr
r=sr.Recognizer()
with sr.AudioFile("sample.wav") as source:
    audio=r.record(source)
text=r.recognize_google(audio,language='jp-JP')
print(text)