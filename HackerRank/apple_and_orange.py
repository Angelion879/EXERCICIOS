def fruitCounter(tree_pos, start_house, end_house, fruit_pos):
    counter = 0

    for i in fruit_pos:
        pos = lambda i: i + tree_pos
        if pos(i) in range(start_house, end_house+1):
            counter+=1

    return counter

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    house_apples = fruitCounter(a,s,t,apples)
    house_oranges = fruitCounter(b,s,t,oranges)

    print(f"{house_apples}\n{house_oranges}")
