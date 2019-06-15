import csv

userMovie = input("Choose the movie: ")
found = False
with open('netflix_ratings.csv','r',newline='') as csvfile:
    movieList = csv.reader(csvfile, delimiter=',')
    
    for title in movieList:
        if userMovie in title:
            found = True
            break
if found: 
    print(f"{title[0]} is rated {title[1]} with a rating {title[-2]} ")
else:
            print("Your title is not in the list :( ")
            found = False