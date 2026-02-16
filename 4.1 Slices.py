# initial list
guests = ['steve jobs', 'abraham lincoln', 'franklin roosevelt']
print(f"{guests[0].title()}, you are invited to my party!")
print(f"{guests[1].title()}, you are invited to my party!")
print(f"{guests[2].title()}, you are invited to my party!")

# revised list
print(f"{guests[0].title()}, {guests[1].title()}, and {guests[2].title()}, I have found a bigger dinner table, so I will invite more guests.")
guests.insert(0, "Lionel Messi")
guests.insert(2, "Winston Churchill")
guests.append("Drake")
guests.sort(key=str.lower)

# new invitations
for guest in guests: 
    print(f"{guest.title()}, you are invited to my larger party!")

# slices
print("The first three items in the list are:")
print(guests[:3])
print("Three items from the middle of the list are:")
print(guests[1:4])
print("The last three items in the list are:")
print(guests[3:])
