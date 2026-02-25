favorite_places = {
    'john': ['the park', 'the movie theatre'],
    'lily': ['the beach'],
    'sam': ['home', 'the lake', 'a football game']           
                }

for name, places in favorite_places.items():
    print(f"\n{name.title()}, where are your favorite places?")
    for place in places:
        print(f"One of my favorite places is {place}.")

