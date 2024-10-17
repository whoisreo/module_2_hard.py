number = int(input("Введите число (от 3 до 20): "))
password = []


if 2 < number < 21:
    for i in range(1, number - 1):
        for j in range(i+1, number):
            if number % (i + j) == 0:
                password.append(i)
                password.append(j)


print(*password)

