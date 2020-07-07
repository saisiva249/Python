'''
A
BB
CCC
DDDD
'''

def sam(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+i), end="")
        print()

sam(4)