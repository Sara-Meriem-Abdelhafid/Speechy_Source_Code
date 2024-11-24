import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone(device_index=0)  # Replace with your microphone's index

with mic as source:
    recognizer.adjust_for_ambient_noise(source)
    print("Listening...")
    audio = recognizer.listen(source)

try:
    print("You said: " + recognizer.recognize_google(audio))
except sr.UnknownValueError:
    print("Sorry, could not understand the audio.")





# Validate the WAV file
def validate_audio_file(file_path):
    import wave
    try:
        with wave.open(file_path, 'rb') as wav_file:
            print(f"Channels: {wav_file.getnchannels()}")
            print(f"Sample width: {wav_file.getsampwidth()}")
            print(f"Frame rate (sample rate): {wav_file.getframerate()}")
            print(f"Number of frames: {wav_file.getnframes()}")
            print("WAV file is valid.")
    except wave.Error as e:
        print(f"Error validating WAV file: {e}")

# Use after saving audio
validate_audio_file(wav_filename)


