
🧠 General Knowledge Quiz Game (KBC Style)

This is a simple Python-based general knowledge quiz game where users answer multiple-choice style questions. Each correct answer rewards 50 points, and the game ends on the first wrong answer.

📋 Features
- 7 general knowledge questions
- Case-insensitive and space-tolerant answer checking
- +50 reward points per correct answer
- Game stops after the first wrong answer

📌 Questions Covered
1. What is the capital city of Australia?
2. Who was the first person to walk on the moon?
3. Which planet is known as the Red Planet?
4. What is the largest ocean on Earth?
5. Who wrote the play 'Romeo and Juliet'?
6. Which is the longest river in the world?
7. In which year did World War II end?

💻 How to Run
Make sure you have Python 3 installed.

1. Save the code in a file named kbc.py
2. Open terminal or command prompt
3. Navigate to the folder where your script is saved
4. Run the program:
   python kbc.py

🧠 Code Logic
- Stores questions and answers in two lists: questions and correct
- Loops through each question and takes user input
- Compares input using strip().lower() for leniency
- Adds 50 points to score for each correct answer
- Exits the loop and ends the game on the first incorrect answer

✅ Example Output
What is the capital city of Australia?
Your answer: canberra
Correct answer ✅
...
Your total reward is: 150

📌 Notes
- Make sure to input exact names (e.g., "Neil Armstrong", not just "Neil").
- The quiz is sensitive to spelling.

📃 License
This project is free to use for educational purposes.
