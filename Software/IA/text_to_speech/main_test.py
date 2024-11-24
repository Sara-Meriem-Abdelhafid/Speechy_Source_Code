import speech_recognition as sr
import playsound
import os

# Helper function to record speech and convert it to text
def record_speech_to_text(chosen_microphone, c, language='en'):
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=chosen_microphone) as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for input...")
        audio = recognizer.listen(source)
        try:
            # Convert speech to text using Google Speech Recognition
            text = recognizer.recognize_google(audio, language=language)
            print(f"Text recorded: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

# Helper function to save text to a file
def input_text_to_file(input_text, c, folder="inputs_folder"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, f"input_text_{c}.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(input_text)
    print(f"Input text saved to: {file_path}")

# Helper function to detect language (you can extend this based on your needs)
def detect_language(input_text):
    # This is a placeholder for detecting language, can use langdetect or other libraries
    language_code = 'ar' if any(char in input_text for char in 'آءأؤإ') else 'en'
    language = "Arabic" if language_code == 'ar' else "English"
    return language_code, language

# Function to generate text based on input text (simple placeholder logic for now)
def gen_text_from_text(input_text):
    # Placeholder: You can integrate more complex logic, e.g., NLP models or APIs
    generated_text = f"Processed Text: {input_text[::-1]}"  # For example, reverse the input text as "generation"
    return generated_text

# Helper function to save generated output to a file
def output_text_to_file(output_text, c, folder="outputs_folder"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, f"output_text_{c}.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(output_text)
    print(f"Generated output text saved to: {file_path}")


# Main script logic to combine everything
def main(chosen_microphone, c):
    # Get input text (record speech and convert to text)
    input_text = record_speech_to_text(chosen_microphone, c, 'ar')  # Use Arabic ('ar') as the default language
    print("\nText recorded:", input_text)
    
    # Save the input text to a file
    input_text_to_file(input_text, c)

    # Detect language
    language_code, language = detect_language(input_text)
    print("\nInput: ", input_text, " in ", language)

    # Generate output text from input text
    gen_output_text = gen_text_from_text(input_text)

    # Save the generated output to a file
    output_text_to_file(gen_output_text, c)

# Example usage (replace chosen_microphone with the appropriate microphone index and c with an identifier)
chosen_microphone = 0  # Example microphone index (adjust based on your system)
c = 1  # Example counter/ID for input-output files
main(chosen_microphone, c)
