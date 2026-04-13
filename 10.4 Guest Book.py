from pathlib import Path
path = Path('guest_list.txt')

guests = []

while True:
    guestName = input("Input your name or enter 'e' to stop new entries: ")

    if guestName.lower() == 'e':
        break
    
    print(f"Welcome to the party, {guestName.title()}!")
    guests.append(guestName)


contents = "Guest List:\n"
for guest in guests:
    contents += guest + "\n"
    
path.write_text(contents)
