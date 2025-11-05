import requests
from rich.console import Console
from rich.table import Table
from player import Player

class PlayerReader:
    def __init__(self, url: str):
        response = requests.get(url, timeout=10).json()
        self.players = []

        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)

    def __iter__(self):
        yield from self.players

class PlayerStats:
    def __init__(self, players):
        self.players = players

    def top_scorers_by_nationality(self, nation):
        suitable = []
        for player in self.players:
            if player.nationality == nation:
                suitable.append(player)
        suitable = sorted(suitable, key=lambda player: player.goals+player.assists, reverse=True)
        return suitable

def make_table(players, season, nationality):
    table = Table(title=f"Season {season} players from {nationality}")

    table.add_column("Released", style="cyan")
    table.add_column("teams", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.goals+player.assists))

    return table

# pylint: disable=too-many-statements
def main():
    console = Console()
    season = console.input("season [magenta](2018-19, 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26)[/magenta]: ")
    url = "https://studies.cs.helsinki.fi/nhlstats/"+season+"/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    #url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    #reader = PlayerReader(url)
    #stats = PlayerStats(reader)
    while True:
        nationality = console.input("nationality [magenta](USA, FIN, CAN, SWE CZE, RUS, SLO, FRA, GBR, SVK, DEN, NED, AUT, BLR, GER, SUI, NOR, UZB, LAT, AUS)[/magenta]: ")
        if nationality == "exit":
            break
        players = stats.top_scorers_by_nationality(nationality)
        table = make_table(players, season, nationality)
        console.print(table)

main()
