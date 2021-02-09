#Exercise:
import sys

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for i in range(len(picture)):
    for j in range(len(picture[i])):
        if(picture[i][j] == 0):
            sys.stdout.write(' ')
        else:
            sys.stdout.write('*')
    print()