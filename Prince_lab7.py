import random
from difflib import get_close_matches
#https://www.geeksforgeeks.org/compare-sequences-in-python-using-dfflib-module/
class TreeNode:
    def __init__(self, team):
        self.team = team
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, team):
        if self.root is None:
            self.root = TreeNode(team)
        else:
            self._insert_recursive(self.root, team)

    def _insert_recursive(self, node, team):
        if team.name < node.team.name:
            if node.left is None:
                node.left = TreeNode(team)
            else:
                self._insert_recursive(node.left, team)
        else:
            if node.right is None:
                node.right = TreeNode(team)
            else:
                self._insert_recursive(node.right, team)

    def inorder_traversal(self):
        teams = []
        self._inorder_traversal_recursive(self.root, teams)
        return teams

    def _inorder_traversal_recursive(self, node, teams):
        if node:
            self._inorder_traversal_recursive(node.left, teams)
            teams.append(node.team)
            self._inorder_traversal_recursive(node.right, teams)

class NFLTeam:
    def __init__(self, name):
        self.name = name

def provide_hint(guess, actual_team):
    close_matches = get_close_matches(guess, [actual_team], n=3, cutoff=0.7)
    if close_matches:
        return f"Did you mean {', '.join(close_matches)}?"
    else:
        return None
#Just wanted to make this a game so it was not completely pointless and had a fun yet technical usage.
def play_guessing_game(bst):
    print("Welcome to the NFL Team Guessing Game!")
    print("You have 4 guesses to identify a randomly selected NFL team.")
    print("After each guess, I'll provide hints to help you narrow down the NFL team.")
    print("Let's begin!\n")

    teams = bst.inorder_traversal()
    random_team = random.choice(teams)

    guesses_left = 4
    while guesses_left > 0:
        print("Guesses left:", guesses_left)
        guess = input("Enter the name of an NFL team: ")

        if guess.lower() == random_team.name.lower():
            print("Congratulations! You've correctly guessed the NFL team:", random_team.name)
            return

        if guess.lower() < random_team.name.lower():
            print("Incorrect. The correct team comes after the team you guessed alphabetically", guess.lower())
        else:
            print("Incorrect. The correct team comes before the team you guessed alphabetically", guess.lower())

        hint = provide_hint(guess.lower(), random_team.name.lower())
        if hint:
            print("Hint:", hint)

        guesses_left -= 1

    print("NOOOO!, you've run out of guesses.")
    print("The correct NFL team was:", random_team.name)

def main():

    teams = [
        NFLTeam("New England Patriots"),
        NFLTeam("Buffalo Bills"),
        NFLTeam("Miami Dolphins"),
        NFLTeam("New York Jets"),
        NFLTeam("Baltimore Ravens"),
        NFLTeam("Pittsburgh Steelers"),
        NFLTeam("Cleveland Browns"),
        NFLTeam("Cincinnati Bengals"),
        NFLTeam("Tennessee Titans"),
        NFLTeam("Indianapolis Colts"),
        NFLTeam("Houston Texans"),
        NFLTeam("Jacksonville Jaguars"),
        NFLTeam("Kansas City Chiefs"),
        NFLTeam("Las Vegas Raiders"),
        NFLTeam("Los Angeles Chargers"),
        NFLTeam("Denver Broncos"),
        NFLTeam("Dallas Cowboys"),
        NFLTeam("Philadelphia Eagles"),
        NFLTeam("New York Giants"),
        NFLTeam("Washington Football Team"),
        NFLTeam("Green Bay Packers"),
        NFLTeam("Minnesota Vikings"),
        NFLTeam("Chicago Bears"),
        NFLTeam("Detroit Lions"),
        NFLTeam("Tampa Bay Buccaneers"),
        NFLTeam("New Orleans Saints"),
        NFLTeam("Atlanta Falcons"),
        NFLTeam("Carolina Panthers"),
        NFLTeam("Los Angeles Rams"),
        NFLTeam("Seattle Seahawks"),
        NFLTeam("San Francisco 49ers"),
        NFLTeam("Arizona Cardinals"),
    ]

    bst = BST()
    for team in teams:
        bst.insert(team)

    play_guessing_game(bst)

if __name__ == "__main__":
    main()
