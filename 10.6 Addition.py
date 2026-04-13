first_number = input("Enter your first number: ")
second_number = input("Enter your second number: ")

try: 
    total = int(first_number) + int(second_number)
    print(f"The total is {total}.")
except ValueError:
    print("Remember to enter your numbers as 1/2/3/etc, not one/two/three/etc.")