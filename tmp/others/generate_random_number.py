# generate random number
import random

low = 1
high = 100
option = ("rock", "paper", "scissor")
cards = ['2,', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# random_number = random.randint(low, high)
# number = random.random() # random pointing float number between 0 and 1
# option = random.choice(option)
# print(option)

random.shuffle(cards)
print(cards)

# I am learning on this youtube channel
# https://www.youtube.com/playlist?list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT
