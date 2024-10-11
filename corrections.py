from data import movies

# You can use the `movies` array here
# Please write every correction and modification of the data to this file by updating the `movies` array

# WRITE YOUR CODE HERE
# adding new plot, years, actors, directors

new_plot_1 = "description about movie"
new_plot_2 = "description about movie"
new_plot_3 = "description about movie"
new_plot_4 = "description about movie"
new_plot_5 = "description about movie"

new_year_1 = "2002"
new_year_2 = "Right year"
new_year_3 = "Right year"
new_year_4 = "Right year"
new_year_5 = "Right year"

new_actors_1 = "NEW NAME1", "Morgan Freeman", "Bob Gunton", "William Sadler"
new_actors_2 = "Tommy Lee Jones", "Javier Bardem", "Josh Brolin", "NEW NAME2"
new_actors_3 = "NEW NAME3", "Mark Ruffalo", "Ben Kingsley", "Max von Sydow"
new_actors_4 = "Adrien Brody", "NEW NAME4", "Michal Zebrowski", "Ed Stoppard"
new_actors_5 = "Samuel L. Jackson", "Kurt Russell", "NEW NAME5", "Walton Goggins"

new_director_1 = "SUPERHERO1"
new_director_2 = "SUPERHERO2"
new_director_3 = "SUPERHERO3"
new_director_4 = "SUPERHERO4"
new_director_5 = "SUPERHERO5"

# adding new genres

new_genres_1 = "Fantasy1"
new_genres_2 = "Fantasy2"

targed_id_1 = 8
targed_id_2 = 31
targed_id_3 = 38
targed_id_4 = 64
targed_id_5 = 82
targed_id_6 = 96
targed_id_7 = 146

# replacing for new data

for movie in movies:
    if movie["id"] == 1:
        movie["plot"] = new_plot_1
    elif movie["id"] == 22:
        movie["plot"] = new_plot_2
    elif movie["id"] == 52:
        movie["plot"] = new_plot_3
    elif movie["id"] == 53:
        movie["plot"] = new_plot_4
    elif movie["id"] == 105:
        movie["plot"] = new_plot_5
    elif movie["id"] == 18:
        movie["year"] = new_year_1
    elif movie["id"] == 27:
        movie["year"] = new_year_2
    elif movie["id"] == 54:
        movie["year"] = new_year_3
    elif movie["id"] == 81:
        movie["year"] = new_year_4
    elif movie["id"] == 102:
        movie["year"] = new_year_5
    elif movie["id"] == 3:
        movie["actors"] = new_actors_1
    elif movie["id"] == 13:
        movie["actors"] = new_actors_2
    elif movie["id"] == 35:
        movie["actors"] = new_actors_3
    elif movie["id"] == 66:
        movie["actors"] = new_actors_4
    elif movie["id"] == 144:
        movie["actors"] = new_actors_5
    elif movie["id"] == targed_id_1:
        movie["director"] = new_director_1
    elif movie["id"] == targed_id_2:
        movie["director"] = new_director_2
    elif movie["id"] == targed_id_3:
        movie["director"] = new_director_3
    elif movie["id"] == targed_id_4:
        movie["director"] = new_director_4
    elif movie["id"] == targed_id_5:
        movie["director"] = new_director_5
    elif movie["id"] == targed_id_6:
        movie["genres"] = new_genres_1
    elif movie["id"] == targed_id_7:
        movie["genres"] = new_genres_2
        break

# adding and replacing new id for movie

old_id = 0
new_id = 90

for movie in movies:
    if movie["id"] == old_id:
        movie["id"] = new_id
        break

# adding new data for movie with id 90

new_title_1 = "Vendetta"
new_year_6 = "2000"
new_runtime_1 = "1.55h"
new_genres_3 = "FANTASY"
new_director_6 = "NEW DIRECTOR"
new_actors_6 = "SAMUEL JACSON"
new_plot_6 = "description about movie"

# Putting new data for movie id 90

for movie in movies:
    if movie["id"] == 90:
        movie["title"] = new_title_1
        movie["year"] = new_year_6
        movie["runtime"] = new_runtime_1
        movie["genres"] = new_genres_3
        movie["director"] = new_director_6
        movie["actors"] = new_actors_6
        movie["plot"] = new_plot_6
        break

print(movies)
