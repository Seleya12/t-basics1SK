import random

# 1. Take User Inputs
width = int(input("Enter the stage width (20-60): "))
height = int(input("Enter the stage height (5-20): "))
instrument = input("Enter your favorite musical instrument: ")

# 2. Validate Inputs (simple version)
if width < 20 or width > 60:
    print("Width out of range, setting to 40.")
    width = 40
if height < 5 or height > 20:
    print("Height out of range, setting to 10.")
    height = 10

# 3. Symbols to use
symbols = ['*', '-', '~', 'o', '.']

# 4. Print top of stage
print("+" + "-" * width + "+")

# 5. Pick a random row for the instrument banner
banner_row = random.randint(1, height - 2)

# 6. Build the stage
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

# 7. Print bottom of stage
print("+" + "-" * width + "+")

# 8. Print audience
audience = "(o_o) "
audience_line = ""
while len(audience_line) < width:
    audience_line += audience

# Only print the right width
print(audience_line[:width])
print(audience_line[:width])

# 9. End message
print("🎶 Thanks for performing on the stage! 🎶")
