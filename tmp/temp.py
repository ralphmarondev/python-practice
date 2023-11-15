# make a string using first middle and last char
def using_first_mid_last_chars(string):
    mid_char = string[len(string)//2]

    new_string = string[0] + mid_char + string[-1]

    return new_string


def using_mid_3_chars(string):
    mid_index = len(string) // 2

    new_string = string[mid_index-1:mid_index+2]

    return new_string


# append new string in the middle of given string
def append_mid_string(string1, string2):
    mid_index = len(string1) // 2
    print(mid_index)

    temp_str = string1[:mid_index:]
    print(temp_str)

    temp_str = temp_str + string2
    print(temp_str)

    new_str = temp_str + string1[mid_index:]

    return new_str
