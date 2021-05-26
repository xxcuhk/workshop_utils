from imdb import IMDb
import pyowm

def get_intent(prediction):
    return prediction["intent"]["intentName"]

def get_entity_type(prediction):
    if (len(prediction["slots"]) > 0):
        return prediction["slots"][0]["entity"]
    else:
        return None

def get_entity_value(prediction):
    if (len(prediction["slots"]) > 0):
        return prediction["slots"][0]["value"]["value"]
    else:
        return None


async def get_weather(city, raw = False):
    owm = pyowm.OWM('b91f88d44ab772a15cfb66d6d3b69cca')
    mgr = owm.weather_manager()

    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place('Hong Kong')
    w = observation.weather
    if raw:
        return {"CurrentTemp": weather.temperature("Celcius"), "SkyCondition": weather.detailed_status}
    else:
        print("The current temperature is" + str(weather.temperature("Celcius")) + "degrees Celcius")
        print("The weather condition is" + str(weather.detailed_status))

    await client.close()



def get_movie_rating(movie_name):
    ia = IMDb()

    # get a movie and print its director(s)
    movie = ia.search_movie(movie_name)
    if (len(movie) == 0):
        print("No movie found with name"+ movie_name)
    else:
        movie = ia.get_movie(movie[0].movieID)
        print(movie_name+" got a rating of "+ str(movie["rating"]) + " out of 10")


def get_movie_directors(movie_name):
    ia = IMDb()

    # get a movie and print its director(s)
    movie = ia.search_movie(movie_name)
    if (len(movie) == 0):
        print("No movie found with name"+ movie_name)
    else:
        movie = ia.get_movie(movie[0].movieID)
        print("The director(s) of "+movie_name + " is/are:")
        for director in movie['directors']:
            print(director['name'])

def get_movie_cast(movie_name):
    ia = IMDb()

    # get a movie and print its director(s)
    movie = ia.search_movie(movie_name)
    if (len(movie) == 0):
        print("No movie found with name" + movie_name)
    else:
        movie = ia.get_movie(movie[0].movieID)
        print("The actors(s) in " + movie_name + " is/are:")
        for actor in movie['cast']:
            print(actor["name"] + " played the role of " + str(actor.currentRole))