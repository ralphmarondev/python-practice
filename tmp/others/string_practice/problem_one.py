# create a new string made of first, middle and last character of each input string
def mix_string(string1, string2):
    first_chars = string1[0] + string2[0]
    mid_chars = string1[int(len(string1) / 2):int(len(string1) / 2) + 1] + \
        string2[int(len(string2) / 2):int(len(string2) / 2) + 1]
    last_chars = string1[-1] + string2[-1]

    return first_chars + mid_chars + last_chars


print(mix_string("America", "Japan"))
