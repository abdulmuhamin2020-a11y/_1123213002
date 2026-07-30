numbers = [10, 20, 20, 30, 40, 50, 60, 80]

new_list = []

for i in numbers:
    if i not in new_list:
        new_list.append(i)

print(new_list)