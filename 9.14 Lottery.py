import random

choices = [1,2,3,4,5,6,7,8,9,10,'A','B','C','D','E']
numbers = choices[:10]
letters = choices[10:]

lottery_numbers = random.sample(numbers, 4)
lottery_letter = random.choice(letters)
winning_result = lottery_numbers + [lottery_letter]

user_numbers = input("Enter 4 numbers, separated by spaces: ").split()
user_letter = input("Enter your bonus letter: ").upper()

user_numbers = [int(num) for num in user_numbers]
user_result = user_numbers + [user_letter]

if user_result == winning_result:
    print("You won the lottery!")
else:
    print("Sorry, you lost.")

print(f"The winning combination is: {winning_result}")