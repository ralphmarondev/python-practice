# format specifier
# format specifier = {value : flags} format a value based on what
#           flags are inserted

price1 = 3.14159
price2 = -987.65
price3 = 12.34

# print(f"Price 1 is: {price1:.3f}")  # display 3 decimal places
# print(f"Price 2 is: {price2:.3f}")

# print(f"Price 3 is: {price1:10}")  # padding of 10
# print(f"Price 3 is: {price2:10}")  # padding of 10
# print(f"Price 3 is: {price3:10}")  # padding of 10

# left justify
print(f"Price 3 is: {price1:<10}")
print(f"Price 3 is: {price2:<10}")
print(f"Price 3 is: {price3:<10}")
print()

# right justify
print(f"Price 3 is: {price1:>10}")
print(f"Price 3 is: {price2:>10}")
print(f"Price 3 is: {price3:>10}")
print()

# centered line
print(f"Price 3 is: {price1:^10}")
print(f"Price 3 is: {price2:^10}")
print(f"Price 3 is: {price3:^10}")

price1 = 3000.14159
price2 = -98670.65
price3 = 1200.34

print(f"Price 1 is: {price1:+,.2f}")
print(f"Price 2 is: {price2:+,.2f}")
print(f"Price 3 is: {price3:+,.2f}")
