n = int(input("Введите число (от 3 до 20): "))
pairs = set()

if 3 <= n <= 20:
    for i in range(1, 21):
        for j in range(1, 21):
            if n == (i + j) or (n % (i + j) == 0 and i != j):
                pairs.add((min(i, j), max(i, j)))

    pair_list = [num for pair in pairs for num in pair]

    print(n, "=", *pair_list)
else:
    print("GG")
