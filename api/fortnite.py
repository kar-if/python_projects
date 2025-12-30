import requests
import pandas as pd

api_key = "9a1bfb36-1a12-4456-a9d3-20101faad4c4"
base_url = "https://fortnite-api.com/v2/stats/br/v2"
headers = {
    "Authorization": api_key
}

def get_fort_info(name):
    params = {"name": name} #player name as query parameter
    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        fort_data = response.json()
        return fort_data
    else:
        print(f"Failed to retrieve data {response.status_code}")
        print(response.text) #helps debug

fortnite_input = input("Enter a player: ")

#fotnite_name = fortnite_input
fortnite_info = get_fort_info(fortnite_input)

rows=[]
if fortnite_info:
    overall = fortnite_info["data"]["stats"]["all"]["overall"]
    account = fortnite_info["data"]["account"]

    rows.append({
        "Name": account["name"],
        "Wins": overall["wins"],
        "Kills": overall["kills"],
        "Matches": overall["matches"],
        "K/D": overall["kd"],
        "Win %": overall["winRate"]
    })

df = pd.DataFrame(rows)
print(df)