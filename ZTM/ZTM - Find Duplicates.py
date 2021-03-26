# Exercise
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []

for item in some_list:
    num = some_list.count(item)
    if num > 1 and item not in duplicates:
        duplicates.append(item)
    else:
        continue
print(duplicates)
