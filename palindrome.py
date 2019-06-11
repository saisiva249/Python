#pallindrome number that is same when written farward and reverse.

i= 232
revnum = 0
temp = i
while i > 0:
    revnum = revnum *10 + (i%10)
    i= i//10
    

print("palindrom number" if temp == revnum  else "not a palindrom")
