'''
    *
   **
  ***
 ****
*****
'''
num = int(input("Enter number of rows"))
for i in range(1,num+1):
    print(" "*(num-i),end="")# helps in ending in same line
    print("*"*i)