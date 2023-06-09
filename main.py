import requests

def get_data(url):
   response = requests.get(url)
   if response.status_code == 200:
       return response.json()
   else:
       return None

def get_character(character_id):
   base_url = "https://swapi.dev/api/people/"
   return get_data(base_url + str(character_id))

def get_planet(planet_url):
   return get_data(planet_url)

def get_starship(starship_url):
   return get_data(starship_url)

# Fetching character information
cheese = input("input a number between 0 and 84 ")
character = get_character(cheese)
if character is not None:
   print("Character: ", character["name"])

   # Fetching homeworld information
   homeworld = get_planet(character["homeworld"])
   if homeworld is not None:
       print("Homeworld: ", homeworld["name"])

   # Fetching starship information
   if character["starships"]:
       for starship_url in character["starships"]:
           starship = get_starship(starship_url)
           if starship is not None:
               print("Starship: ", starship["name"])
   else:
       print("No starships found for this character.")
else:
   print("Character not found.")