N = int(input())
factorial = int(1)
count = int(2)
summa = int(2)

if N > 1:
    while count <= N:
        factorial = factorial * count
        summa = summa + 1/factorial
        count = count + 1
    print(summa)
if N == 0:
    print(1)
if N == 1:
    print(2)