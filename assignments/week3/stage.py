import random


width = int(input("Enter the stage width (20-60): "))
height = int(input("Enter the stage height (5-20): "))
instrument = input("Enter your favorite musical instrument: ")

if width < 20 or width > 60:
    print("Width out of range, setting to 40.")
    width = 40
if height < 5 or height > 20:
    print("Height out of range, setting to 10.")
    height = 10

symbols = ['*', '-', '~', 'o', '.']

print("+" + "-" * width + "+")

banner_row = random.randint(1, height - 2)

for row in range(height):
    line = "|"
    for col in range(width):
        if row == banner_row:
            # Center the instrument
            start_col = (width - len(instrument)) // 2
            if start_col <= col < start_col + len(instrument):
                line += instrument[col - start_col]
            else:
                line += " "
        else:
            # Randomly pick symbol or space
            if random.randint(1, 5) == 1:
                line += random.choice(symbols)
            else:
                line += " "
    line += "|"
    print(line)

print("+" + "-" * width + "+")

audience = "(o_o) "
audience_line = ""
while len(audience_line) < width:
    audience_line += audience

print(audience_line[:width])
print(audience_line[:width])

print("🎶 Thanks for performing on the stage! 🎶")
