# Initial prompt.
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")

# Final version with revision.
alien_color = 'blue'

if alien_color == 'green':
    score = 5
elif alien_color == 'yellow':
    score = 10
elif alien_color == 'red':
    score = 15
else:
    score = 0

if score >= 5:
    print(f"You just earned {score} points!")
else:
    print("Oh no, you earned zero points!")