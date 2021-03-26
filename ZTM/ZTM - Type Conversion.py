import datetime

birth_year = int(input('What year were you born? '))
this_year = datetime.datetime.now()
age = int(this_year.year) - birth_year
print(f'your age is: {age}')
