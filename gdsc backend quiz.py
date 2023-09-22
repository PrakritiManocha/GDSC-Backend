def run_quiz():
    question_data = [
        {"text": "A slug's blood is green.", "answer": "True"},
        {"text": "The loudest animal is the African Elephant.", "answer": "False"},
        {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
        {"text": "The total surface area of a human lung is the size of a football pitch.", "answer": "True"},
        {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
        {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
        {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
        {"text": "You can lead a cow downstairs but not upstairs.", "answer": "False"},
        {"text": "Google was originally called 'Backrub'.", "answer": "True"},
        {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
        {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
        {"text": "A few ounces of chocolate can kill a small dog.", "answer": "True"}
    ]

    print("Welcome to the True/False Quiz!")

    def display_question(question_text):
        print(question_text)

    def get_user_answer():
        while True:
            user_input = input("Your answer (True/False): ").strip().capitalize()
            if user_input in ['True', 'False']:
                return user_input
            else:
                print("Invalid input. Please enter 'True' or 'False'.")

    def calculate_score(questions_and_answers):
        score = 0
        for question_data in questions_and_answers:
            question_text = question_data["text"]
            correct_answer = question_data["answer"]

            display_question(question_text)
            user_answer = get_user_answer()

            if user_answer == correct_answer:
                score += 1

        return score

    final_score = calculate_score(question_data)

    print("Your final score is:", final_score/len(question_data))

run_quiz()
