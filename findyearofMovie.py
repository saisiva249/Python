#pip install IMDbPY
import imdb

#creating the instance of IMDB
im = imdb.IMDb()

#getting the movie with name
search = im.search_movie("Sye Raa Narasimha Reddy")

#getting movie released year
year = search[0]['year']

#printing name and year of movie
print(search[0]['title']+ " realeased in " + str(year))
