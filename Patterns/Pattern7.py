'''
1
23
456
78910
1112131415
'''

def num(n):
    num =1
    for i in range(1,n):
        for j in range(1,i+1):
            print(num, end="")
            num+=1
        print()
        

num(6)