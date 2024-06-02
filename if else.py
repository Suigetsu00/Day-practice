print("Printing current and previous number sum in a range (10)")

pn = 0

for i in range(1, 11):
    xs = pn + i
    print("Current number", i, "Previous number", pn, "Sum: ", xs)

    pn = i