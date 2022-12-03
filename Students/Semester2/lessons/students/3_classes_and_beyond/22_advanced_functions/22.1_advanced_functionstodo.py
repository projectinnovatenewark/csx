"""
Solidify learning of functions and combine loops/conditions within them
"""

#  Imagine it's 3 games into the NFL season. Theres two conferences, each with four divisions.
#  Each division has four teams. Each team has played three games.
#  The first score will always be the listed team's score.

week_three_nfl_standings = {
    "AFC": {
        "East": {
            "Buffalo Bills": [[12, 20], [23, 30], [30, 10]],
            "Miami Dolphins": [[40, 42], [40, 30], [15, 19]],
            "New England Patriots": [[10, 10], [50, 10], [42, 30]],
            "New York Jets": [[10, 30], [20, 40], [15, 50]]
        },
        "South": {
            "Houston Texans": [[32, 45], [25, 6], [30, 40]],
            "Indianapolis Colts": [[40, 20], [11, 18], [15, 19]],
            "Jacksonville Jaguars": [[20, 3], [25, 20], [27, 45]],
            "Tennessee Titans": [[34, 6], [3, 10], [29, 34]]
        },
        "North": {
            "Baltimore Ravens": [[33, 10], [40, 20], [15, 12]],
            "Cincinnati Bengals": [[25, 28], [25, 20], [40, 20]],
            "Cleveland Browns": [[29, 34], [30, 22], [25, 34]],
            "Pittsburgh Steelers": [[15, 19], [10, 3], [25, 28]]
        },
        "West": {
            "Denver Broncos": [[15, 19], [10, 6], [40, 20]],
            "Kansas City Chiefs": [[40, 20], [11, 18], [15, 19]],
            "Oakland Raiders": [[25, 28], [6, 18], [10, 18]],
            "San Diego Chargers": [[29, 34], [30, 22], [25, 34]]
        }
    },
    "NFC": {
        "East": {
            "Dallas Cowboys": [[15, 19], [10, 3], [25, 28]],
            "New York Giants": [[32, 45], [25, 6], [30, 40]],
            "Philadelphia Eagles": [[40, 20], [11, 18], [15, 19]],
            "Washington Redskins": [[20, 3], [25, 20], [27, 45]]
        },
        "South": {
            "Atlanta Falcons": [[29, 34], [30, 42], [40, 53]],
            "Carolina Panthers": [[20, 3], [25, 20], [27, 45]],
            "New Orleans Saints": [[32, 45], [25, 6], [30, 40]],
            "Tampa Bay Buccaneers": [[15, 19], [10, 3], [25, 28]]
        },
        "North": {
            "Chicago Bears": [[29, 34], [30, 42], [40, 53]],
            "Detroit Lions": [[40, 20], [11, 18], [15, 19]],
            "Green Bay Packers": [[25, 28], [25, 20], [40, 20]],
            "Minnesota Vikings": [[29, 34], [30, 22], [25, 34]]
        },
        "West": {
            "Arizona Cardinals": [[20, 3], [25, 20], [27, 45]],
            "St. Louis Rams": [[25, 28], [25, 20], [40, 20]],
            "San Francisco 49ers": [[10, 3], [21, 28], [29, 34]],
            "Seattle Seahawks": [[29, 34], [30, 42], [40, 53]]
        },
    }
}

# note: you are welcome to create 'helper functions' or smaller functions that make solving these
# problems easier.

def team_statistics():
    # TODO: print out each team's name followed by their average score, lowest and highest score

def first_place_teams():
    # TODO: find the first place team in each division and print out their record in a readable way

def highest_scoring_team():
    # TODO: find the highest score of a team in each conference
    # TODO: i.e. AFC highest scoring team is the Baltimore Ravens and NFC highest scoring team is the New York Giants

def tied_a_game():
    # TODO: there was a tie in one game. find the team and print the score

def division_leader(division):
    # TODO: find the team in the lead of the division provided (AFC or NFC)