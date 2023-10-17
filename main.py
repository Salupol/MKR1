import random
n = int(input("Введіть розмірність масиву:"))
array = [[random.randint(0,3) for _ in range(n)] for _ in range(n)]
print("Початковий масив")
for row in array:
    print(row)
column_sums = [0] * n
for i in range(n):
    for row in array:
        column_sums[i] += row[i]
print("\nСуми для кожної колонки:")
print(column_sums)
sorted_columns = sorted(range(n), key=lambda x: column_sums[x])
sorted_array = [[row[i] for i in sorted_columns] for row in array]

print("\nВідсортований масив:")
for row in sorted_array:
    print(row)