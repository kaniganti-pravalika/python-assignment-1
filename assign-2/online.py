# Project 4: Online Exam System


def start_exam():
    questions = [
        {
            "question": "1. What is the capital of India?",
            "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
            "answer": "B"
        },
        {
            "question": "2. Which keyword is used to define a function in Python?",
            "options": ["A. function", "B. define", "C. def", "D. fun"],
            "answer": "C"
        },
        {
            "question": "3. What is 10 * 5?",
            "options": ["A. 50", "B. 40", "C. 60", "D. 55"],
            "answer": "A"
        },
        {
            "question": "4. Which data type is used to store text?",
            "options": ["A. int", "B. float", "C. string", "D. bool"],
            "answer": "C"
        },
        {
            "question": "5. Which symbol is used for comments in Python?",
            "options": ["A. //", "B. #", "C. /* */", "D. --"],
            "answer": "B"
        }
    ]


    score = 0


    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)


        user_answer = input("Enter your answer (A/B/C/D): ").upper()


        if user_answer == q["answer"]:
            print("Correct Answer!")
            score += 1
        else:
            print("Wrong Answer! Correct answer is", q["answer"])


    total_questions = len(questions)
    percentage = (score / total_questions) * 100


    print("\n===== Final Result =====")
    print("Your Score:", score, "out of", total_questions)
    print("Percentage:", percentage, "%")


    if percentage >= 80:
        print("Grade: A")
    elif percentage >= 50:
        print("Grade: B")
    else:
        print("Result: Fail")




# Main program loop for retake option
while True:
    start_exam()
    choice = input("\nDo you want to retake the exam? (Y/N): ").upper()
    if choice != "Y":
        print("Thank you for participating!")
        break


