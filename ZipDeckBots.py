import random

class Player(object):
    def __init__(self, player_num):
        self.player_num = player_num
    def play(self, card, info):
        # Info is a hash containing the number of players, the round number, and every player's score
        # Ex: info = {"player_count": 4, "round": 2, "scores": {0: 2, 1: 0, 2: 2, 3: 6, 4: 5} }

        # Define your own play function for your class.

        # If you think you're highest, return an array where the first element is the
        # phrase "Zip Deck!", and the second is a dictionary for how you'd assign points
        # if you win.
        # E.g. ["Zip Deck!", {0: 2, 1: 2, 4: 1}]

        # If you don't think you're highest, return an array with one element, the empty
        # string (or anything that's not "Zip Deck!")

        return [""]

class Rando(Player):
    def play(self, card, info):
        if random.random() > 0.5:
            target = {i for i in range(info["player_count"])} - {self.player_num}
            target = random.choice(tuple(target))
            points = card//4
            return ["Zip Deck!", {target: points}]
        else:
            return [""]
