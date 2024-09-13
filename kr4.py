N = int(input())
zero_counter = int(0)
count = int(1)
x = int(0)

if N >= 0:
    while count <= N:
        x = N % 10
        if x == 0:
            zero_counter = zero_counter + 1
        N = N // 10
        count = count + 1
    print(zero_counter)