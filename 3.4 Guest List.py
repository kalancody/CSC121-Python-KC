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
guests.sort()

# new invitations
print(f"{guests[0].title()}, you are invited to my larger party!")
print(f"{guests[1].title()}, you are invited to my larger party!")
print(f"{guests[2].title()}, you are invited to my larger party!")
print(f"{guests[3].title()}, you are invited to my larger party!")
print(f"{guests[4].title()}, you are invited to my larger party!")
print(f"{guests[5].title()}, you are invited to my larger party!")