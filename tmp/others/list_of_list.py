fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

# print(groceries[1][0])  # prints 'celery'

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
