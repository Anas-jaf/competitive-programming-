# https://codeforces.com/problemset/problem/263/A

axe1 = [int(x) for x in input().split()]
axe2 = [int(x) for x in input().split()]
axe3 = [int(x) for x in input().split()]
axe4 = [int(x) for x in input().split()]
axe5 = [int(x) for x in input().split()]
matrix = []
rowNum=0
for x in range(1 ,6):

    matrix += [globals()['axe%s' % x] ]

    if (1 in globals()['axe%s' % x]):
        oneishere = globals()['axe%s' % x]
        rowNum = x

print ((abs(oneishere.index(1)- 2)) +(abs(rowNum - 3)))

