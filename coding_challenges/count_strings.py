'''

Name: Count Sub-Strings
Task:
Given a string, S, and a substring - count the number of times the substring appears.

Sample Input:
ABCDCDC
CDC

Sample Output:
2
'''

def count_substring(string,sub_string):
    counter = 0
    length = len(sub_string)
    for i in range(len(string)):
        if (string[i] == sub_string[0]):
            if (string[i:(i+length)] == sub_string):
                counter += 1
        else:
            pass
    return counter

string = input().strip()
sub_string = input().strip()
count = count_substring(string,sub_string)
print(count)
