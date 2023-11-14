# learning about dictionaries
# dictionary = collection of {key:values} pairs
#               ordered and changeable. No duplicates
capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"
            }

# print(dir(capitals))
# print(help(capitals))

# get data in our dictionary returns 'None' if not exists
# print(capitals.get("USA"))

# if capitals.get("Russia"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# print(capitals)
# capitals.update({"Germany": "Berlin"})
# print(capitals)

# capitals.pop("China")

# capitals.popitem()

# capitals.clear()

# keys = capitals.keys()
# print(keys)

# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#     print(value)

# items = capitals.items()
# print(items)

for key, value in capitals.items():
    print(f"{key} : {value}")
