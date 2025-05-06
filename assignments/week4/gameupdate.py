import time

# Game constants
MAX_HP = 100
ATTEMPTS = 5
DEBUG = False  

# Asks a multiple-choice question and checks if the answer is correct
def ask_question(question, options, correct_letter):
    print(question)
    letters = ['a', 'b', 'c']
    for letter, option in zip(letters, options):
        print(f"{letter.upper()}) {option}")
    answer = input("Your answer (A-C): ").strip().lower()

    if answer == correct_letter:
        print("Correct!")
        return True
    else:
        print(f"Incorrect! The correct answer was {correct_letter.upper()}) {options[letters.index(correct_letter)]}.")
        return False

# Checks if the user can guess the correct release year
def check_year():
    print("\nWhat year was 'Meteora' released?")
    year = input("Enter a year between 2000 and 2010: ")
    if year.isdigit():
        year = int(year)
        if year == 2003:
            print("Boom! Right on the money.")
            return True
        else:
            print("Close, but it was 2003.")
            return False
    else:
        print("That wasn't a number.")
        return False

# User can choose between the two singers
def check_choice():
    print("\nDo you prefer Emily's screaming or Mike's rapping?")
    choice = input("Type 'screaming' or 'rapping': ").strip().lower()
    if choice == 'screaming':
        print("YEAHHHHHHHH 🔥 Let's break something!")
        return True
    elif choice == 'rapping':
        print("Yo, you're vibin' with Fort Minor energy. I respect that.")
        return True
    else:
        print("You're a peaceful soul, huh?")
        return False

# Main quiz function that tracks score
def quiz():
    score = 0

    if ask_question(
        "Which album features the song 'The Emptiness Machine'?",
        ["Meteora", "Minutes to Midnight", "From Zero"],
        'c'):
        score += 1

    if ask_question(
        "Finish the lyric: 'I tried so hard...'",
        ["...and got so far", "...to fall apart", "...but lost it all"],
        'a'):
        score += 1

    if check_year():
        score += 1

    check_choice()  # <-- Kein Punkt mehr hier

    if ask_question(
        "Which song includes the lyrics: 'Put me out of my misery'?",
        ["One More Light", "Given Up", "Crawling"],
        'b'):
        score += 1

    return score

# Displays final result based on score
def print_result(score, name):
    print(f"\n🎤 Quiz complete, {name}! You scored {score}/4.")
    if score == 4:
        print("You're a Linkin Legend! ⭐⭐⭐⭐⭐")
    elif score >= 3:
        print("Solid! You know your LP. 🤘")
    else:
        print("Looks like it's time for a re-listen marathon 🎧")

# Ask if user wants to play again
def play_again():
    response = input("\nDo you want to play again? (yes/no): ").strip().lower()
    return response == "yes"

# Entry point for the quiz
def start_quiz():
    print("\n🎧 Welcome to the Linkin Park Song Quiz! 🎧")
    time.sleep(1)

    name = input("What's your name, soldier? ")
    print(f"Nice to meet you, {name}! Let's see if you're a true Linkin Park fan...")
    time.sleep(1)

    while True:
        score = quiz()
        print_result(score, name)

        print("\nThanks for playing! Keep the LP spirit alive. 💀🎸")

        if not play_again():
            print("Goodbye! 👋")
            break
            
# Start quiz
if __name__ == "__main__":
    start_quiz()
