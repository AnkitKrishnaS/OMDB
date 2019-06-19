import sys

API_KEY = "568b125"

# if using the module level client

# omdb.set_default('568b125', API_KEY)

print("The arguments are: ", str(sys.argv))

if len(sys.argv) > 2:

    movie_name = "%20".join(sys.argv[1:len(sys.argv)])

    print(movie_name)

else:

    movie_name = sys.argv[1]

url = "http://www.omdbapi.com/?t=" + movie_name + "&apikey=568b125"

print(url)

# must use OMDb API parameters

# include full plot and Rotten Tomatoes data

import requests

resp = requests.get(url, json={"key": "value"})

print(resp.json())

json_data = resp.json()

Rotten_Tomato_rating = ""

for key, value in json_data.items():

    if (key == "Ratings"):

        for item in value:

            if item["Source"] == 'Rotten Tomatoes':

                Rotten_Tomato_rating = item['Value']

            else:

                pass

print("******* Rotten_Tomato_rating for " + str(movie_name) + "is : ", Rotten_Tomato_rating)