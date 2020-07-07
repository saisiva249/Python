'''
*
**
***
****
***
**
*
'''
def patrn(n):
    for i in range(1,n+1):
        print("*"*i)
    for i in range(1,n):
        print("*"*(n-i))

patrn(6)
