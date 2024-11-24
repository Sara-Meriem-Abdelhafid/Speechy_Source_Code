'''from gtts import gTTS
from playsound import playsound

# Arabic text
text = "مرحباً! كيف يمكنني مساعدتك؟"

# Convert to speech
tts = gTTS(text=text, lang='ar')
tts.save("output.mp3")
playsound("output.mp3")







engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Find Arabic voice
for voice in voices:
    if "ar" in voice.languages:
        engine.setProperty('voice', voice.id)
        break

engine.say("مرحباً! كيف يمكنني مساعدتك؟")
engine.runAndWait()



import pyttsx3

engine = pyttsx3.init()

# List all voices and choose by ID
voices = engine.getProperty('voices')
selected_voice_id = voices[2].id  # Replace '2' with the desired voice index
engine.setProperty('voice', selected_voice_id)

# Test speaking with the selected voice
engine.say("مرحباً، كيف حالك؟")
engine.runAndWait()


import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
for index, voice in enumerate(voices):
    print(f"Voice #{index}:")
    print(f" - ID: {voice.id}")
    print(f" - Name: {voice.name}")
    print(f" - Languages: {voice.languages}")
    print(f" - Gender: {voice.gender if hasattr(voice, 'gender') else 'Unknown'}\n")
'''
from google.cloud import texttospeech

def text_to_speech_google(text, language_code="ar-XA", gender="MALE"):
    # Initialize the client
    client = texttospeech.TextToSpeechClient()

    # Configure the voice
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )

    # Configure the audio settings
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Build the synthesis request
    synthesis_input = texttospeech.SynthesisInput(text=text)
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Save the audio to a file
    output_file = "output.mp3"
    with open(output_file, "wb") as out:
        out.write(response.audio_content)
        print(f"Audio content written to {output_file}")

    # Play the audio
    import playsound
    playsound.playsound(output_file)

# Example usage
text_to_speech_google("مرحباً، كيف حالك؟")
