rivers = {'russia': 'volga', 'germany': 'elbe', 'france': 'seine'}

# Prints a sentence for each river
for country, river in rivers.items():
    print(f"the {river.title()} River runs through {country.title()}.")

# Uses a loop to print countries in the dictionary
for country in rivers.keys():
    print(f"{country.title()} is a country included in this dictionary.")

# Uses a loop to print rivers in the dictionary
for river in rivers.values():
    print(f"The {river.title()} is a river included in this dictionary.")
