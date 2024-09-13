x = int(input())
n = float(0)
count = int(1)

while count <= x:
    n = n + 1/(count**2)
    count = count + 1
print("Result", n)
    