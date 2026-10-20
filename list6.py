questions = [
    "What is 2 + 2?",
    "Which language uses print()?",
    "What is 5 * 3?"
]
answers = ["4", "Python", "15"]
score = 0
for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Your answer: ")
    if user_answer.strip().lower() == answers[i].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! Answer:", answers[i])
print("Final Score:", score, "/", len(questions))