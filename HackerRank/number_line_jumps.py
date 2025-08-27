def kangaroo(x1, v1, x2, v2):
    # Write your code here
    dist = x2-x1
    if v1>v2 and (dist%(v1-v2)==0):
        return "YES"
    else:
        return "NO"