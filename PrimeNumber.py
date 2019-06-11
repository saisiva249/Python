#print prime number in a range of numbers

i= 1
while i<20:
    j= 1       
    count = 0 
    while j<= i:
            if i%j == 0:
                count = count +1
            j = j +1
    else:
        if(count >2):
            print("{} is consonent number".format(i))
        else:
            print ("{} is prime number".format(i))
    i = i+1
