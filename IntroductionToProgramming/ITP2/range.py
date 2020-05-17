a, b, c = (int(X) for X in input().split())

if a < b and b < c:
    print('Yes')
else:
    print('No')