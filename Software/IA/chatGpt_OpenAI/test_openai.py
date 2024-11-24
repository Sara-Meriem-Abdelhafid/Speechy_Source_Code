import openai

# You need to set your OpenAI API key here
openai.api_key = 'your-api-key'

def generate_answer(input_question):
    # Query GPT-3 for an answer to the question
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can also use other models
        prompt=input_question,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract and return the answer text from the response
    answer = response.choices[0].text.strip()
    return answer

# Example Usage
input_question = "What is the capital of France?"
output_answer = generate_answer(input_question)
print(f"Question: {input_question}")
print(f"Answer: {output_answer}")
