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
'''import speech_recognition as sr
from pydub import AudioSegment
import io

# Initialize recognizer
recognizer = sr.Recognizer()

# Record audio using recognizer
with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)
    print("Listening...")
    audio = recognizer.listen(source)

# Convert the raw audio to a pydub AudioSegment
audio_data = io.BytesIO(audio.frame_data)
audio_segment = AudioSegment.from_wav(audio_data)

# Skip the first 3 seconds of audio
skip_seconds = 3
skip_ms = skip_seconds * 1000  # Convert to milliseconds
trimmed_audio = audio_segment[skip_ms:]

# Save the new audio file
trimmed_audio.export("trimmed_audio.wav", format="wav")

print("Trimmed audio saved to 'trimmed_audio.wav'")
'''
