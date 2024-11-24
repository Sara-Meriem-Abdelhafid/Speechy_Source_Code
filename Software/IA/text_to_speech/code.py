'''import speech_recognition as sr
import pyttsx3


r = sr.Recognizer() 



 # type: ignore
'''
import pyttsx3
import os
from tempfile import NamedTemporaryFile

def text_to_speech_wav(text, lang="en"):
    if not text.strip():
        return  # Return if there is no text to convert

    # Configure pyttsx3
    engine = pyttsx3.init()
    
    # Set language if needed
    voices = engine.getProperty("voices")
    if lang == "en":
        engine.setProperty("voice", voices[0].id)  # English voice
    elif lang == "ar":
        for voice in voices:
            if "arabic" in voice.name.lower():
                engine.setProperty("voice", voice.id)
                break
    
    # Save text-to-speech as a .wav file
    with NamedTemporaryFile(delete=False, suffix=".wav") as tmp_wav:
        tmp_wav_path = tmp_wav.name
        engine.save_to_file(text, tmp_wav_path)
        engine.runAndWait()

    # Play the generated .wav file
    play_audio(tmp_wav_path)

    # Optionally, clean up the temporary file
    os.unlink(tmp_wav_path)

def play_audio(file_path):
    import simpleaudio as sa
    
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until the sound has finished playing

# Example Usage
text_to_speech_wav("Hello, how are you?", "en")
