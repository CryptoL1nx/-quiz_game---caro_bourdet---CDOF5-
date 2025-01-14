import random
from colorama import init, Fore

# Initialisation de colorama
init(autoreset=True)

# Bank of 30 questions on advanced investment topics (bonds, cryptocurrencies, and taxation)
QUESTIONS_BANK = [
    {
        "question": "What is the primary factor affecting bond prices?",
        "options": ["Interest rates", "Stock market trends", "Real estate prices", "Consumer spending"],
        "answer": "Interest rates"
    },
    {
        "question": "What is a zero-coupon bond?",
        "options": [
            "A bond with no maturity date",
            "A bond that does not pay periodic interest",
            "A bond issued by the government",
            "A bond with a variable interest rate"
        ],
        "answer": "A bond that does not pay periodic interest"
    },
    {
        "question": "What is the term for the initial sale of a cryptocurrency to the public?",
        "options": ["Initial Coin Offering (ICO)", "Crypto Launch", "Token Generation Event", "Digital Fundraising"],
        "answer": "Initial Coin Offering (ICO)"
    },
    {
        "question": "What is the tax rate typically applied to long-term capital gains in many countries?",
        "options": ["Lower than short-term gains", "Higher than short-term gains", "The same as short-term gains", "Not taxable"],
        "answer": "Lower than short-term gains"
    },
    # More questions can be added following the same structure
]

def print_divider():
    """Affiche un diviseur ASCII simple pour séparer les sections"""
    print("\n" + "=" * 40 + "\n")

def print_welcome():
    """Affiche un message de bienvenue avec de l'ASCII art"""
    print("""
     __     ______  _    _   _      ____   _____ ______ 
     \ \   / / __ \| |  | | | |    / __ \ / ____|  ____|
      \ \_/ / |  | | |  | | | |   | |  | | (___ | |__   
       \   /| |  | | |  | | | |   | |  | |\___ \|  __|  
        | | | |__| | |__| | | |___| |__| |____) | |____ 
        |_|  \____/ \____/  |______\____/|_____/|______|
    """)

def ask_question(question):
    """Pose une question de quiz avec une deuxième chance en cas de mauvaise réponse."""
    print("\n" + question['question'])
    for i, option in enumerate(question['options'], start=1):
        print(f"{i}. {option}")

    for attempt in range(2):
        try:
            answer = int(input("Enter the number of your answer: "))
            if 1 <= answer <= len(question['options']):
                if question['options'][answer - 1] == question['answer']:
                    print(Fore.GREEN + "Correct! 🎉")
                    return True if attempt == 0 else False
                else:
                    print(Fore.RED + "Incorrect.")
                    if attempt == 0:
                        print("Try again (no points for this attempt).")
            else:
                print("Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"The correct answer was: {question['answer']}")
    return False

def main():
    """Fonction principale pour exécuter le quiz."""
    print_welcome()
    print("Welcome to the Advanced Banking Investment Quiz!")
    print("Test your knowledge of bonds, cryptocurrencies, and taxation in finance!")

    selected_questions = random.sample(QUESTIONS_BANK, 5)

    score = 0
    errors = []

    for question in selected_questions:
        ask_question(question)
        print_divider()

    print(f"\nYour final score is: {score}/5")

    if errors:
        print("\nHere are the questions you missed with their correct answers:")
        for error in errors:
            print(f"- {error['question']}\n  Correct answer: {error['answer']}")

    print("\nThank you for playing!")

if __name__ == "__main__":
    main()
