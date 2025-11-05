class Player:
    def __init__(self, dictionary: dict):
        self.name = dictionary['name']
        self.nationality = dictionary["nationality"]
        self.goals = dictionary["goals"]
        self.assists = dictionary["assists"]
        self.team = dictionary["team"]

    def __str__(self):
        return f"{self.name:20}{self.team:15}{self.goals:>2} + {self.assists:<2} = {self.goals+self.assists}"
