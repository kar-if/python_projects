import requests, random

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(pokemon_id):
    url = f"{base_url}/pokemon/{pokemon_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_input = input(int("Would you like to 1. Search or 2. Trade Pokemon? "))

poke_random = random.randint(1, 1025)

pokemon_info = get_pokemon_info(poke_random)

# pokemon_name = pokemon_input
# pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")