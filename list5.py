numbers = [20, 30, 40, 50, 60, 70, 80]

reverse = []
index = len(numbers) - 1

while index >= 0:
    reverse.append(numbers[index])
    index -= 1

print(reverse)