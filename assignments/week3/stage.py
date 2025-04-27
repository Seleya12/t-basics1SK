import random
import time

# Step 1: User Inputs
width = int(input("Enter the stage width (20-60): "))
height = int(input("Enter the stage height (5-20): "))
instrument = input("Enter your favorite musical instrument: ")

# Validation
if width < 20 or width > 60 or height < 5 or height > 20:
    print("Stage size out of bounds! Using default (40x10).")
    width = 40
    height = 10

# Easy typing "music" symbols
music_symbols = ['*', '-', '~', 'o', '.', "'", '|']

# Step 2: Create the top border
print('+' + '-' * width + '+')

# Random row where the instrument name will appear
banner_row = random.randint(1, height - 2)

for row in range(height):
    line = '|'
    for col in range(width):
        if row == banner_row:
            # Insert the instrument centered
            start_pos = (width - len(instrument)) // 2
            if start_pos <= col < start_pos + len(instrument):
                line += instrument[col - start_pos]
            else:
                line += ' '
        else:
            # Randomly place symbols or spaces
            if random.random() < 0.15:
                line += random.choice(music_symbols)
            else:
                line += ' '
    line += '|'
    print(line)
    time.sleep(0.1)  # small delay for animation

# Stage floor
print('+' + '-' * width + '+')

# Step 3: Create audience row
audience = "(o_o)"
audience_line = ''
while len(audience_line) < width:
    audience_line += audience + ' '
# Truncate audience line to match width
audience_line = audience_line[:width]

# Print audience under the stage
print(' ' + audience_line)
print(' ' + audience_line)

print("\n🎶 Thanks for performing on the stage! 🎶")
