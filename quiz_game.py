import random
quiz_data = [
    {
        "question": "What is the capital of India?",
        "choices": ["A. London", "B. New Delhi", "C. Rome", "D. Berlin"],
        "answer": "B"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["A. Mercury", "B. Venus", "C. Jupiter", "D. Saturn"],
        "answer": "C"
    },
    {
        "question": "What is the chemical symbol for water?",
        "choices": ["A. O2", "B. H2O", "C. CO2", "D. NaCl"],
        "answer": "B"
    }
]

def display_welcome():
    print("Welcome to the Quiz Game !")
    print("Rules: Select the correct answer from the given choices.")
    print("Let's get started!\n")

def present_question(question_data):
    print(question_data["question"])
    for choice in question_data["choices"]:
        print(choice)
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
    return user_answer

def evaluate_answer(question_data, user_answer):
    correct_answer = question_data["answer"]
    if user_answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        print(f"The correct answer is: {correct_answer}")
        return 0

def calculate_final_score(score, total_questions):
    return int(score / total_questions * 100)

def display_results(score, total_questions):
    print("\n--- Quiz Completed! ---")
    print(f"Your Score: {score}/{total_questions}")
    percentage = calculate_final_score(score, total_questions)
    if percentage >= 80:
        print("Great job! You did well.")
    elif 60 <= percentage < 80:
        print("Good effort! Keep practicing.")
    else:
        print("Keep studying. You can do better!")

def play_again():
    return input("\nDo you want to play again? (yes/no): ").lower().startswith("y")

def main():
    display_welcome()

    total_questions = len(quiz_data)
    score = 0

    while True:
        random.shuffle(quiz_data)
        for question_data in quiz_data:
            user_answer = present_question(question_data)
            score += evaluate_answer(question_data, user_answer)

        display_results(score, total_questions)

        if not play_again():
            break

        score = 0
        print("\nLet's play again!\n")

if __name__ == "__main__":
    main()