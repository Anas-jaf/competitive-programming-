# 69A - Young Physicist
# http://codeforces.com/problemset/problem/69/A


n = int(input())
sum = 0

for x in range(n):
    axe = [int(x) for x in input().split()]
    for j in range(2):
        sum += axe[j]

if (sum == 0):
    print("YES")
else:
    print("NO")
