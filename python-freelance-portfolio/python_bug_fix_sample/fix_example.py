# コード（バグあり）

numbers = [10, 20, 30]

total = 0

for i in range(len(numbers)+1):
    total += numbers[i]

print(total)


# コード（バグなし）

numbers = [10, 20, 30]

total = 0

for number in numbers:
    total += number

print("Total:", total)