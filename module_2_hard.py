number = int(input("Введите число (от 3 до 20): "))
password = []


if 3 <= number < 21:
    for i in range(1, number - 1):
        for j in range(i+1, number - 1):
            if number % (i + j) == 0:
                password.append(i)
                password.append(j)


print(*password)

