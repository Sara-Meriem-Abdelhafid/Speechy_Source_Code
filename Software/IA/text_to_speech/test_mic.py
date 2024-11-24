import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()  # Replace with your microphone's index

with mic as source:
    recognizer.adjust_for_ambient_noise(source)
    print("Listening...")
    audio = recognizer.listen(source)

try:
    print("You said: " + recognizer.recognize_google(audio))
except sr.UnknownValueError:
    print("Sorry, could not understand the audio.")
