#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Tommy', 2)
cat2 = Cat('Aurora', 1)
cat3 = Cat('Astolfo', 1)

# 2 Create a function that finds the oldest cat
def old_cat(catlist):
    older = 0
    for i in range(0,len(catlist)):
        if catlist[i].age > older:
            older = catlist[i].age
    return older

cats = [cat1,cat2,cat3]
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f'The oldest cat is {old_cat(cats)} years old')