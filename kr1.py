n = int(0)
before = int(0)
count = int(0)

while count < 2:
    print("Entre digit")
    x = int(input())
    if x >= 0:
        n = n + x
        if x == 0 and count == 0:
            count = count + 1
            before = x
        elif x == 0 and count == 1 and before == 0:
            count = count + 1
        elif x == 0 and count == 1 and before != 0:
            count = 0
    else:
        print("Invalid digit")
print("Result:", n)