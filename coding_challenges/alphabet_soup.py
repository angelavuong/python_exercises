def AlphabetSoup(new_name):
    new_name = ''.join(sorted(new_name))
    return new_name

user_input = raw_input("Type a string: ")
print (str(user_input) + " becomes " + str(AlphabetSoup(user_input)))
