import time
import random

print("\n🎧 Welcome to the Linkin Park Song Quiz! 🎧")
time.sleep(1)

name = input("What's your name, soilder ? ")
print("Nice to meet you,", name + "! Let's see if you're a true Linkin Park fan...")
time.sleep(1)

score = 0

# Question 1
print("\n1. Which album features the song 'The emptiness Machine'?")
print("A) Meteora")
print("B) Minutes to Midnight")
print("C) From Zero")
answer1 = input("Your answer: ").strip().lower()
if answer1 == 'c':
    print("Correct! Starting strong.")
    score += 1
else:
    print("Oops! That was from 'From Zero'.")

# Question 2 (with nested if)
print("\n2. Finish the lyric: 'I tried so hard...'")
print("A) ...and got so far")
print("B) ...to fall apart")
print("C) ...but lost it all")
answer2 = input("Your answer: ").strip().lower()
if answer2 == 'a':
    print("Yep, classic line.")
    score += 1
    if score == 2:
        print("You're on fire! 🔥")
else:
    print("Nope, it's '...and got so far'!")

# Question 3 (number input — only one check)
print("\n3. What year was 'Meteora' released?")
year = input("Enter a year between 2000 and 2010: ")

# check if it's a number
if year.isdigit():
    year = int(year)
    if year == 2003:
        print("Boom! Right on the money.")
        score += 1
    elif year >= 2000 and year <= 2010:
        print("Close, but it was 2003.")
    else:
        print("That year is out of the range.")
else:
    print("That wasn't a number.")

# Question 4 (branching)
print("\n4. Do you prefer Emily's screaming or Mike's rapping?")
choice = input("Type 'screaming' or 'rapping': ").strip().lower()
if choice == 'screaming':
    print("YEAHHHHHHHH 🔥 Let's break something!")
elif choice == 'rapping':
    print("Yo, you're vibin' with Fort Minor energy. I respect that.")
else:
    print("You're a peaceful soul, huh?")

# Question 5
print("\n5. Which song includes the lyrics : 'Put me out of my misery'?")
print("A) One More Light")
print("B) Given Up")
print("C) Crawling")
answer5 = input("Your answer: ").strip().lower()
if answer5 == 'b':
    print("YES! That's a powerful opener.")
    score += 1
else:
    print("That's from 'Given Up'. Screams included.")

# Final Score
print("\n🎤 Quiz complete,", name + "! You scored", score, "/4.")
if score == 4:
    print("You're a Linkin Legend! ⭐⭐⭐⭐⭐")
elif score >= 3:
    print("Solid! You know your LP. 🤘")
else:
    print("Looks like it's time for a re-listen marathon 🎧")

print("\nThanks for playing! Keep the LP spirit alive. 💀🎸")
