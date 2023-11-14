# string indexing
# indexing = accessing elements of a sequence using []
# (indexing operator) [start : end : step]

cute_name = "ralph-maron-is-cute"

# print(cute_name[0])
# print(cute_name[0:5]) # start -> includex; end -> excluded
# print(cute_name[6:11]) # prints maron
# print(cute_name[6:])  # prints from index 6 to the last
# print(cute_name[-1]) # accessing elements from last [using negative indexing]
# print(cute_name[::2]) # print every 2nd char
# print(cute_name[::3]) # print every 3rd char

# last_chars = cute_name[-4:]  # only 4 chars visible
# print(f"xxxxx-xxxxx-xx-{last_chars}")

print(cute_name[::-1])  # reverse string
