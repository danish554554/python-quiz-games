questions = [
    "What is the capital city of Australia?",
    "Who was the first person to walk on the moon?",
    "Which planet is known as the Red Planet?",
    "What is the largest ocean on Earth?",
    "Who wrote the play 'Romeo and Juliet'?",
    "Which is the longest river in the world?",
    "In which year did World War II end?"
]

correct = ["Canberra", "Neil Armstrong", "Mars", "Pacific Ocean", "William Shakespeare", "Nile River", "1945"]

score = 0  # initialize reward score

for i in range(len(questions)):
    print(questions[i])
    ans = input("Your answer: ")
    if ans.strip().lower() == correct[i].lower():
        print("Correct answer ✅")
        score += 50
    else:
        print("You are wrong ❌")
        break

print("Your total reward is:", score) #final reward
