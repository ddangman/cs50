movies = [
    {"title": "Green Book", "year": 2018},
    {"title": "The Shape of Water", "year": 2017},
    {"title": "Moonlight", "year": 2016},
    {"title": "Spotlight", "year": 2015},
    {"title": "Birdman", "year": 2014},
    {"title": "12 Years a Slave", "year": 2013}
]

# key=lambda(parameter) parameter: return parameter["key"] 
movies.sort(key=lambda movie: movie["year"])

for movie in movies:
    print("{title} was released in {year}".format(**movie))


games = [
    {"title": "Metal Gear Solid", "year": 1998},
    {"title": "Gears of War", "year": 2006},
    {"title": "Resident Evil", "year": 1996},
    {"title": "Mortal Kombat", "year": 1992},
    {"title": "God of War", "year": 2005},
    {"title": "Doom", "year": 1993}
]

def get_title(media):
    return media["title"]

def get_year(media):
    return media["year"]

games.sort(key=get_title)
for game in games:
    print("{title} was released in {year}".format(**game))