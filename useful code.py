# useful code 

# variable of variable
for x in range(0, 9):
    globals()['string%s' % x] = 'Hello'
# string0 = 'Hello', string1 = 'Hello' ... string8 = 'Hello'



# wrap a list of numbers in list array
[int(x) for x in input().split()]

