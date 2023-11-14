# collection = single 'variable' used to store multiple values
# List   = [] ordered and changeable. Duplicates OK
# Set    = {} ordered and immutable, but Add/Remove OK. No duplicates
# Tuple  = () ordered and unchangeable. Duplicates OK. FASTER

class Collections:
    def display(self, value):
        print(value)

    def list_demo(self):
        fruits = ["apple", "orange", "banana", "coconut"]

        self.display(fruits)

        # # reverse
        # self.display(fruits[::-1])

        # # print item from index 0 to index 2; 3 is excluded :<
        # self.display(fruits[0:3])

        # # lengths
        # self.display(len(fruits))

        # # boolean
        # self.display("pineapple" in fruits)

        # # changing data
        # fruits[0] = "pineapple"
        # self.display(fruits)

        # fruits.append("pineapple")
        # self.display(fruits)

        # fruits.remove("apple")
        # self.display(fruits)

        # fruits.insert(0, "pineapples")
        # self.display(fruits)

        # fruits.sort()

        # fruits.reverse()

        # fruits.clear()

        print(fruits.index("apple"))

        print(fruits.count("banana"))

    def set_demo(self):
        fruits = {"apple", "orange", "banana", "coconut"}

        # print(len(fruits))
        # print("pineapple" in fruits)
        # fruits.add("pineapple")
        # fruits.remove("apple")
        # fruits.pop() # can be stored to a variable
        # fruits.clear()

        print(fruits)

    def tuple_demo(self):
        fruits = ("apple", "orange", "banna", "coconut")

        # print(len(fruits))
        # print("pineapple" in fruits)

        # print(fruits.index("apple"))
        print(fruits.count("coconut"))

        print(fruits)


if __name__ == "__main__":
    collection = Collections()

    collection.tuple_demo()
