# list of question
# store the answer
# randomely pick questions 
# ask the questions
# see if they are correct
# keep tack of the score 
# tell the use the score

import random

questions = {
    1: "What is a List in Python? Explain its features.",
    2: "How do you create and access elements in a Python list?",
    3: "Explain List Slicing in Python with examples.",
    4: "Differentiate between List and Tuple in Python.",
    5: "Explain commonly used List Methods in Python.",
    6: "How can you add, update, and delete elements from a list?",
    7: "Write a program to find the largest and smallest element in a list.",
    8: "Write a program to reverse a list.",
    9: "What is List Comprehension in Python? Explain with examples.",
    10: "Write a program to remove duplicate elements from a list."
}

def python_trivia_game():
    question_list = list(questions.keys())
    total_question = 5
    score = 0

    selected_questions = random.sample(question_list, total_question)
    
    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}.{question}")
        user_answer = input("Your answer:").lower().strip()

        correct_answer = question[question]

        if user_answer == correct_answer.lower():
            print("corect !\n")
            score == 1
        else:
            print(f"Wrong. The correct answer is : {correct_answer}.\n")
    print(f"game over! your final score is : {score}/{total_question}")

python_trivia_game()