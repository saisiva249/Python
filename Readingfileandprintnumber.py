@author: venkata sai siva
"""
#reading text in each line of a file and print line number at end

filepath = 'sampleText.txt'  
with open(filepath) as file:
    lineread = file.readline()
    count = 1
    while lineread:
        print ("{} {}".format(lineread.strip(), count))
        lineread = file.readline()
        count = count +1
