import random

n = int(input("Введіть розмірність масиву:"))
while True:
    try:
        a = int(input("Введіть нижню межу чисел в масиві:"))
        b = int(input("Введіть верхню межу чисел в масиві:")) # розкоментувати для вибору верхньої та верхньої межі чисел
        break
    except ValueError:
        print("Введені некоректні числа, спробуйте ще раз")
array = [[random.randint(a, b) for _ in range(n)] for _ in range(n)]  # генеруемо масив
print("Початковий масив:")
for row in array:
    print(row)  # виводимо початковий масив
column_sums = [0] * n
for i in range(n):
    for row in array:
        column_sums[i] += row[i]  # рахуемо суму колонок масиву
print("\nСуми для кожної колонки:")
print(column_sums)  # виводимо
sorted_columns = sorted(range(n),
                        key=lambda x: column_sums[x])  # використовуємо лямдба-функцію як критерій сотрування колонок
sorted_array = [[row[i] for i in sorted_columns] for row in array]  # сортуемо колонки по сумі

print("\nВідсортований масив:")
for row in sorted_array:
    print(row)  # виводимо на екран
