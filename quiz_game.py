import random

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
    {
        "question": "What is the significance of a bond's credit rating?",
        "options": [
            "It determines the bond's maturity date",
            "It reflects the issuer's ability to repay the debt",
            "It affects the bond's liquidity",
            "It indicates the bond's historical price performance"
        ],
        "answer": "It reflects the issuer's ability to repay the debt"
    },
    {
        "question": "What does a yield curve inversion typically indicate?",
        "options": [
            "Upcoming economic growth",
            "Potential economic recession",
            "Stable inflation",
            "High investor confidence"
        ],
        "answer": "Potential economic recession"
    },
    {
        "question": "What is the primary purpose of stablecoins in cryptocurrency?",
        "options": [
            "To hedge against inflation",
            "To provide price stability",
            "To maximize returns",
            "To fund blockchain projects"
        ],
        "answer": "To provide price stability"
    },
    {
        "question": "Which type of bond is issued by corporations and is not backed by collateral?",
        "options": ["Convertible bonds", "Debenture bonds", "Municipal bonds", "Treasury bonds"],
        "answer": "Debenture bonds"
    },
    {
        "question": "What is a blockchain in the context of cryptocurrency?",
        "options": [
            "A chain of smart contracts",
            "A distributed ledger technology",
            "A cryptocurrency trading strategy",
            "A type of mining algorithm"
        ],
        "answer": "A distributed ledger technology"
    },
    {
        "question": "What does the term 'duration' refer to in bond investment?",
        "options": [
            "The bond's time to maturity",
            "The bond's sensitivity to interest rate changes",
            "The bond's credit quality",
            "The bond's liquidity"
        ],
        "answer": "The bond's sensitivity to interest rate changes"
    },
    {
        "question": "What is a capital gains tax?",
        "options": [
            "A tax on bond interest income",
            "A tax on profits from selling assets",
            "A tax on dividends",
            "A tax on gross income"
        ],
        "answer": "A tax on profits from selling assets"
    },
    {
        "question": "What is a junk bond?",
        "options": [
            "A bond with a short maturity",
            "A bond with a low credit rating",
            "A bond issued by startups",
            "A bond with no interest payment"
        ],
        "answer": "A bond with a low credit rating"
    },
    {
        "question": "Which of the following is NOT a type of tax applied in finance?",
        "options": ["Value-added tax", "Income tax", "Liquidity tax", "Capital gains tax"],
        "answer": "Liquidity tax"
    },
    {
        "question": "What is staking in cryptocurrency?",
        "options": [
            "Buying and holding a coin for profit",
            "Using cryptocurrency as collateral",
            "Participating in a network's proof-of-stake system",
            "Paying for transaction fees"
        ],
        "answer": "Participating in a network's proof-of-stake system"
    },
    {
        "question": "What is an investment-grade bond?",
        "options": [
            "A bond with a high credit rating",
            "A bond with a short maturity",
            "A bond with a high yield",
            "A bond issued by a startup"
        ],
        "answer": "A bond with a high credit rating"
    },
    {
        "question": "What is the purpose of a bond's coupon payment?",
        "options": [
            "To pay back the principal",
            "To compensate the bondholder with periodic interest",
            "To provide liquidity",
            "To increase the bond's yield"
        ],
        "answer": "To compensate the bondholder with periodic interest"
    },
    {
        "question": "What is a cryptocurrency wallet?",
        "options": [
            "A digital tool for mining coins",
            "A device for storing private keys",
            "An account for trading on exchanges",
            "A tax tool for cryptocurrency"
        ],
        "answer": "A device for storing private keys"
    },
    {
        "question": "Which tax principle applies to cross-border investments?",
        "options": [
            "Double taxation agreements",
            "Single-tier taxation",
            "Tax-free zones",
            "Flat rate taxation"
        ],
        "answer": "Double taxation agreements"
    },
    # More questions can be added following the same structure
]

def print_divider():
    """Print a divider for better UI."""
    print("\n" + "=" * 50 + "\n")

def ask_question(question, question_number, total_questions):
    """Ask a single quiz question with a second chance for incorrect answers."""
    print_divider()
    print(f"Question {question_number}/{total_questions}")
    print(question['question'])
    for i, option in enumerate(question['options'], start=1):
        print(f"{i}. {option}")

    for attempt in range(2):
        try:
            answer = int(input("Enter the number of your answer: "))
            if 1 <= answer <= len(question['options']):
                if question['options'][answer - 1] == question['answer']:
                    print("\033[92mCorrect! 🎉\033[0m")  # Green text for correct
                    return True if attempt == 0 else False
                else:
                    print("\033[91mIncorrect.\033[0m")  # Red text for incorrect
                    if attempt == 0:
                        print("Try again (no points for this attempt).")
            else:
                print("Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"The correct answer was: \033[94m{question['answer']}\033[0m")  # Blue text for correct answer
    return False

def main():
    """Main function to run the quiz game."""
    print("\033[96mWelcome to the Advanced Banking Investment Quiz!\033[0m")
    print("Test your knowledge of bonds, cryptocurrencies, and taxation in finance!")

    selected_questions = random.sample(QUESTIONS_BANK, 5)

    score = 0
    errors = []

    for i, question in enumerate(selected_questions, start=1):
        if ask_question(question, i, len(selected_questions)):
            score += 1
        else:
            errors.append(question)

    print_divider()
    print(f"\033[93mYour final score is: {score}/{len(selected_questions)}\033[0m")

    if errors:
        print("\033[91mHere are the questions you missed with their correct answers:\033[0m")
        for error in errors:
            print(f"- {error['question']}\n  Correct answer: \033[94m{error['answer']}\033[0m")

    print("\033[96m\nThank you for playing!\033[0m")

if __name__ == "__main__":
    main()
