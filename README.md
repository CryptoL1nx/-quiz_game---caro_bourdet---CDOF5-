#### Decentralization-Technologies  

# Advanced Banking Investment Quiz

## Description
The **Advanced Banking Investment Quiz** is a Python-based console application designed to test and educate users on advanced investment concepts. The quiz covers topics like bonds, cryptocurrencies, and taxation in finance. It features a bank of 30 questions, with 5 random questions selected for each session.

Key features include:
- Randomized questions for every quiz.
- Educational second-chance attempts for incorrect answers.
- Final score display with corrections for errors.

---

## Prerequisites
- Python 3.7 or later installed.
- A code editor like [Visual Studio Code](https://code.visualstudio.com/) (recommended).

---

## Setup Instructions

### 1. Clone the Repository
If you are using Git, clone the repository:
```bash
git clone <repository_url>
```
Otherwise, download and extract the project ZIP file.

### 2. Open the Project in VS Code
1. Launch Visual Studio Code.
2. Open the folder containing the project files (`quiz_game.py`).

### 3. Install Python Dependencies (if any)
If you decide to expand the project to include external libraries in the future, set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate   # On Windows
```
Currently, no additional libraries are required.

---

## How to Run the Quiz

1. Open a terminal in the project folder.
2. Run the following command:
   ```bash
   python quiz_game.py
   ```
3. Answer the questions as they appear in the terminal.

---

## Gameplay Instructions

1. **Start the Quiz**: The program will display 5 random questions from the question bank.
2. **Answer Questions**: 
   - Enter the number corresponding to your chosen option.
   - If you answer incorrectly, you’ll get a second chance (no points awarded for the second attempt).
3. **View Results**:
   - At the end of the quiz, your score will be displayed along with the corrections for any mistakes.

---

## Example Output

```
Welcome to the Advanced Banking Investment Quiz!
Test your knowledge of bonds, cryptocurrencies, and taxation in finance!

1. What is the primary factor affecting bond prices?
1. Interest rates
2. Stock market trends
3. Real estate prices
4. Consumer spending
Enter the number of your answer: 1
Correct! 🎉

...

Your final score is: 4/5

Here are the questions you missed with their correct answers:
- What does a yield curve inversion typically indicate?
  Correct answer: Potential economic recession

Thank you for playing!
```

---

## Customization
You can expand the question bank by modifying the `QUESTIONS_BANK` list in `quiz_game.py`.

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## License
This project is open source and available under the [MIT License](LICENSE).

---

## Contact
For questions or feedback, please reach out to:
- **Email**: your-email@example.com
- **GitHub**: [YourGitHubUsername](https://github.com/YourGitHubUsername)

