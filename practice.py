import requests, random
base_url = "https://pokeapi.co/api/v2/"
pokemon_list = []

def get_pokemon_info(pokemon_id):
    url = f"{base_url}/pokemon/{pokemon_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

poke_range = 3
random_ids = random.sample(range(1, 1026), poke_range)
print("Hello! Your starting 3 Pokemon are:")
for poke_id in random_ids:
    pokemon_info = get_pokemon_info(poke_id)
    if pokemon_info:
        print("---------------")
        print(f"Name: {pokemon_info["name"].capitalize()}")
        print(f"ID: {pokemon_info["id"]}")
        print(f"Height: {pokemon_info["height"]}")
        print(f"Weight: {pokemon_info["weight"]}")

        pokemon_list.append(pokemon_info)

pokemon_input = input("Would you like to 1) Search or 2) Trade Pokemon? ").lower()

if pokemon_input == "1":
    poke_search = input("Which Pokemon would you like to search? ")
    poke_search = get_pokemon_info(poke_search)
    if poke_search:
        print(f"Name: {poke_search["name"].capitalize()}")
        print(f"ID: {poke_search["id"]}")
        print(f"Height: {poke_search["height"]}")
        print(f"Weight: {poke_search["weight"]}")
        
elif pokemon_input == "2":
    poke_range = 3
    random_ids = random.sample(range(1, 1026), poke_range)

print("Your random Pokemons are: ")
for poke_id in random_ids:
    pokemon_info = get_pokemon_info(poke_id)

    if pokemon_info:
            print("---------------")
            print(f"Name: {pokemon_info["name"].capitalize()}")
            print(f"ID: {pokemon_info["id"]}")
            print(f"Height: {pokemon_info["height"]}")
            print(f"Weight: {pokemon_info["weight"]}")

    poke_trade = input("Which of your Pokemon would you like to trade? ").lower()
    pokemon_list.remove(poke_trade)


    #input(f'Which Pokemon are you trading {poke_trade} for? ')
else:
    print("Invalid input")