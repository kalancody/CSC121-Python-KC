peoples = input("How many people are in your group? ")

totalCost = 0
i = 0

while i < int(peoples):
    age = input(f"\nHow old is person #{i + 1} in your group? ")

    if int(age) > 12:
        totalCost = totalCost + 15
        print(f"This person's ticket costs $15.")
    elif int(age) > 3:
        totalCost = totalCost + 10
        print(f"This person's ticket costs $10.")
    elif int(age) < 3:
        print(f"Anyone under 3 gets in free!")
    i += 1

print(f"The total cost for all of the tickets is ${totalCost}.")