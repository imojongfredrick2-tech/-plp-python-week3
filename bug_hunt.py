count = 1
total = 0

# BUG: The while statement was missing a colon, so I added ':' at the end.
while count <= 5:
    # BUG: The condition was count < 5, which skipped the number 5.
    total = total + count
    count = count + 1

# BUG: total is an integer, so I converted it to a string before joining it with the text.
print("Sum of 1 to 5 is: " + str(total))