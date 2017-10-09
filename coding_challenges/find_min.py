n = [0,5,10,6,-1,9]

i = 0

def find_max():
    global i
    max_value = n[i]
    i += 1

    while (i < len(n)):
        if (max_value < n[i]):
            max_value = n[i]
            i += 1
        else:
            i += 1
    return max_value

def find_min():
    i = 0
    min_value = n[i]
    i += 1

    while (i < len(n)):
        if (min_value > n[i]):
            min_value = n[i]
            i += 1
        else:
            i += 1
    return min_value

print "Min value: " + str(find_min())
print "Max value: " + str(find_max())
