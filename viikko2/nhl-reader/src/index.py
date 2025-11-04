import requests
from player import Player

def players_by_nationality(players: list, nation: str):
    suitable = []
    for player in players:
        if player.nationality == nation:
            suitable.append(player)
    return suitable

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    nation = "FIN"
    filtered_players = players_by_nationality(players, nation)
    sorted_players = sorted(filtered_players, key=lambda player: player.goals+player.assists, reverse=True)
    print(f"Players from: {nation}")

    for player in sorted_players:
        print(player)

main()