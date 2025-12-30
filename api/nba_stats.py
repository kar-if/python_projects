# python3 api/nba_stats.py

import pandas as pd
from nba_api.live.nba.endpoints.scoreboard import ScoreBoard

sb = ScoreBoard()
games = sb.games.get_dict()

rows = []
for g in games:
    rows.append({
        "away": g["awayTeam"]["teamTricode"],
        "home": g["homeTeam"]["teamTricode"],
        "away_score": g["awayTeam"]["score"],
        "home_score": g["homeTeam"]["score"],
        "status": g["gameStatusText"]
    })

df = pd.DataFrame(rows)
print(df)

