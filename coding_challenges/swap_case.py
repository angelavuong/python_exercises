'''

Name: Swap Case

Task: A single line containing a string S.

Sample Input:
HackerRank.com presents "Pythonist 2".

Sample Output:
hACKERrANK.COM PRESENTS "pYTHONIST 2".
'''

def swap_case(s):
    new_string = s.swapcase()
    return new_string

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
