'''

Name: What's Your Name?

Task: You are given the first name and last name of a person on two different lines. Your task is to read them and print the following:
Hello <firstname> <lastname>! You just delved into python.


Sample Input:
Guido
Rossum

Sample Output:
Hello Guido Rossum! You just delved into python.
'''

def print_full_name(a, b):
    print("Hello " + a + " " + b + "! You just delved into python.")

if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)
