def highest_even(li):
    high = 0
    for item in li:
        if item % 2 ==0 and item >= high:
            high = item
    return high
print(highest_even([10,2,3,4,8,11]))