def hanoi(n, start, end):
    if n == 1:
        print("Move disc", n, "from", start, "->", end)
    else:
        other = 6 - (start + end)
        hanoi(n - 1, start, other)
        print("Move disc", n, "from", start, "->", end)
        hanoi(n - 1, other, end)

m = int(input("Enter the number of discs: "))
hanoi(m, 1, 3)
