'''

Name: String Split and Join

Task:  You are given a string. Split the string on a ' ' delimiter and join using a - hyphen.

Sample Input:
this is a string

Sample Output:
this-is-a-string
'''

def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result
