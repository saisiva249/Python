'''
@author: venkata sai siva
'''

#reading text in each line of a file and print line number at end

filepath = 'sampleText.txt'  
with open(filepath) as file:
    #intialization for first line
    lineread = file.readline()
    count = 1
    #for iteration over the next lines
    while lineread:
        print ("{} {}".format(lineread.strip(), count))
        lineread = file.readline()
        count = count +1
