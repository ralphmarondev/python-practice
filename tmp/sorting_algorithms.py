class SortingAlgorithms:
    def bubble_sort(num: list):
        lenght = len(num)

        for i in range(lenght):
            for j in range(0, lenght-1-i):
                if num[j] > num[j + 1]:
                    num[j], num[j + 1] = num[j + 1], num[j]

    def quick_sort(self, num: list):
        lenght = len(num)

        if lenght <= 1:
            return num

        pivot = num[lenght // 2]
        left = [x for x in num if x < pivot]
        right = [x for x in num if x > pivot]
        middle = [x for x in num if x == pivot]

        return self.quick_sort(left) + middle + self.quick_sort(right)
