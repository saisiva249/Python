'''
* * * * *
 * * * *
  * * *
    *
  * * *
 * * * *
* * * * *
'''
def pat(n):
    for i in range(n):
        print(" "*i+"* "*(n-i))
    for i in range(2,n+1):
        print(" "*(n-i)+"* "*i)
    
pat(5)