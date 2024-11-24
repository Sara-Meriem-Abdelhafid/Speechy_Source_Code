def generate_answer(input_question):
    # Convert the question to lowercase to make the matching case-insensitive
    input_question = input_question.lower()

    # Define a set of predefined questions and corresponding answers in Arabic
    question_answer_pairs = {
    "what is your name": "I am Speechy.",
    "how are you": "I'm doing well, thank you for asking!",
    "what can you do": "I can help with a variety of tasks, such as answering questions, providing information, and more.",
    "who are you": "I am your Robot friend designed to assist you.",
    "tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
    "what is the weather like": "I currently can't check the weather, but I can help with other tasks.",

    "ما اسمك": "أنا Speechy.",
    "كيف حالك": "أنا بخير، شكراً على سؤالك!",
    "ماذا يمكنك أن تفعل": "يمكنني مساعدتك في العديد من المهام، مثل الإجابة على الأسئلة، تقديم المعلومات، وأكثر.",
    "من أنت": "أنا صديقك الروبوت المصمم لمساعدتك.",
    "أخبرني نكتة": "لماذا لا يقاتل الهياكل العظمية بعضهم البعض؟ لأنهم ليس لديهم الشجاعة!",
    "كيف الطقس": "لا أستطيع التحقق من الطقس حالياً، لكن يمكنني مساعدتك في أمور أخرى.",
        "ما اسمك": "أنا مساعد ذكي.",
        "كيف حالك": "أنا بخير، شكراً على سؤالك!",
        "ماذا يمكنك أن تفعل": "يمكنني مساعدتك في العديد من المهام مثل الإجابة على الأسئلة، تقديم المعلومات، وتوليد النصوص.",
        "من أنت": "أنا مساعد ذكي مصمم لمساعدتك.",
        "أخبرني نكتة": "لماذا لا يقاتل الهياكل العظمية بعضهم البعض؟ لأنهم ليس لديهم الشجاعة!",
        "كيف الطقس": "لا أستطيع التحقق من الطقس حالياً، لكن يمكنني مساعدتك في أمور أخرى."
    }

    # Check if the input question matches any predefined questions
    for question, answer in question_answer_pairs.items():
        if question in input_question:
            return answer

    # Default response if no match is found
    return "عذراً، لا أفهم هذا السؤال."

# Example Usage
input_question = "ما اسمك؟"
output_answer = generate_answer(input_question)
print(f"السؤال: {input_question}")
print(f"الإجابة: {output_answer}")




 
