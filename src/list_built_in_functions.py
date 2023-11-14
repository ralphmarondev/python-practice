class ListBuiltInFunctions:
    my_list = [1, 2, 3, 4, 5]

    def conditional_filtering(self):
        # filtering element greater than 1
        filtered_list = list(filter(lambda x: x > 1, self.my_list))

        return filtered_list

    def mapping(self):
        # multiplying each element by 2
        mapped_list = list(map(lambda x: x * 2, self.my_list))

        return mapped_list

    def reducing(self):
        from functools import reduce

        # multiply each element in the list
        product = reduce(lambda x, y: x * y, self.my_list)

        return product

    def enumerating(self):
        # returns an enumerate object containing pairs of index and element
        enumerated_list = list(enumerate(self.my_list, start=0))

        return enumerated_list

    def zipping(self):
        # combines elements from multipple iterable into tuples
        my_list2 = ['a', 'b', 'c', 'd', 'e']

        zipped_list = list(zip(self.my_list, my_list2))

        return zipped_list

    def membership_testing(self):
        # check if 3 is present in 'self.my_list'
        return 3 in self.my_list

    def conversion(self):
        # converts an iterable (e.g. tuple, string) to a list
        my_tuple = (1, 2, 3)

        converted_list = list(my_tuple)

        return converted_list

    def slicing_and_striding(self):
        # return the element from 1 to 4 - 1
        sliced_list = self.my_list[1:4]

        return sliced_list

    def display(self, value):
        print(value)


if __name__ == "__main__":
    built_in = ListBuiltInFunctions()

    # print the list
    built_in.display(built_in.my_list)

    # print the filtered list
    built_in.display(built_in.conditional_filtering())

    # print the reduced list
    built_in.display(built_in.reducing())

    # print the enumerated list
    built_in.display(built_in.enumerating())

    # print the zipped list
    built_in.display(built_in.zipping())

    # membership testing
    built_in.display(built_in.membership_testing())

    # conversion
    built_in.display(built_in.conversion())

    # slicing
    built_in.display(built_in.slicing_and_striding())
