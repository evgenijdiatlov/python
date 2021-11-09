import requests
import pprint

response = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=1118')

# print(response.json())

list_of_pokemons = response.json()['results']
pokemon_names = [x['name'] for x in list_of_pokemons]
print(pokemon_names)
