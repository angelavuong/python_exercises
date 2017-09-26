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
    count = 0
    word_count = 0
    check_word = []
    length = len(sub_string)
    for i in range(len(string)):
        if (string[i] == sub_string[0] and i-len(sub_string) <= 1):
            for j in range(len(sub_string)):
                check_word.append(string[i])
                i+=1
            final_string = ''.join(check_word)
            if(final_string == sub_string):
                count += 1
                check_word = []
            else:
                pass
        else:
            pass
    return count

string = input().strip()
sub_string = input().strip()
count = count_substring(string,sub_string)
print(count)
