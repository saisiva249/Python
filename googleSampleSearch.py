#package required Google
from  googlesearch import search

keyword = "Learn Python"

#tld: top level domain com, co.uk, co.in 
#num: number of results to be searched
#stop: when to stop search, here after 10 results search will stop, if used NONE then it will be searching forever
#pause: 
for search_item in search(keyword,tld='co.in',num=10,stop=10,pause=2):
    print(search_item)