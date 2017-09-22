'''
Name: Apple and Orange
Task:
- d = units of distance from its tree origin along x-axis. Negative value means fruit fell to tree's left. Positive value means fruit fell to tree's right.
- s = house start point
- t = house end point
- a = apple tree Location
- b = orange tree Location

Output:
- Count number of fruits that fall within house region
'''
#!/bin/python3

import sys
def fruit_calculator(house_start,house_end,fruit,tree_location):
    fruit_counter = 0
    for each in fruit:
        if(each + tree_location >= house_start and each + tree_location <= house_end):
            fruit_counter += 1
        else:
            pass
    return fruit_counter

# House Coordinates
s,t = input().strip().split(' ')
s,t = [int(s),int(t)]

# Apple(a) and Orange(b) Coordinates
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]

# Location of fruit drops
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]

apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

apple_count = fruit_calculator(s,t,apple,a)
orange_count = fruit_calculator(s,t,orange,b)
print(apple_count)
print(orange_count)
