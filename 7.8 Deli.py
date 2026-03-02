sandwich_orders = ['cuban', 'reuben', 'italian','sub', 'chicken salad']
finished_sandwiches = []

while sandwich_orders:
    print(f"I just made your {sandwich_orders[0].title()} Sandwich.")
    finished_sandwiches.append(sandwich_orders[0])
    sandwich_orders.pop(0)

print(f"\nI have made the following sandwiches:")
for sandwich in finished_sandwiches:
    print(f"-{sandwich.title()} Sandwich.")