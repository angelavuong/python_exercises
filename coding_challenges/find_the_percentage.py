'''

Name: Find the Percentage

Task:
The first line contains integer N, the number of students.
The next N lines contains the name and marks obtained by that student separated by a space.
The final line contains the name of a particular student previously listed.

Sample Input:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output:
56.00
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    result = 0
    for i in range(len(student_marks[query_name])):
        result = student_marks[query_name][i] + result
    result = result/3
    print('%.2f'%result)
