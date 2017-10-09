'''

Name: Text Wrap

Task: You are given a string, S, and a width, w.
Your task is to wrap the string into a paragraph of width w.

Sample Input:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

'''

import textwrap

def wrap(string, max_width):
    result = textwrap.fill(string,max_width)
    return result

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result
