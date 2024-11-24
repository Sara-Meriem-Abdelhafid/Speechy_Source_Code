def generate_answer(input_question):
    # Convert the question to lowercase to make the matching case-insensitive
    input_question = input_question.lower()

    # Define a set of predefined questions and corresponding answers
    question_answer_pairs = {
        "what is your name": "I am a helpful assistant.",
        "how are you": "I'm doing well, thank you for asking!",
        "what can you do": "I can help with a variety of tasks, such as answering questions, providing information, and generating text.",
        "who are you": "I am an AI designed to assist you.",
        "tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
        "what is the weather like": "I currently can't check the weather, but I can help with other tasks."
    }

    # Check if the input question matches any predefined questions
    for question, answer in question_answer_pairs.items():
        if question in input_question:
            return answer

    # Default response if no match is found
    return "I'm sorry, I don't understand that question."

# Example Usage
input_question = "What is your name?"
output_answer = generate_answer(input_question)
print(f"Question: {input_question}")
print(f"Answer: {output_answer}")
