import random

class Player(object):
    def __init__(self, my_num, player_count):
        self.my_num = my_num
        self.player_count = player_count
    def play(self, card, info):
        # Info is a hash containing the round number and every player's score
        # Ex: info = {"round": 2, "scores": {0: 2, 1: 0, 2: 2, 3: 6, 4: 5} }

        # Define your own play function for your class.

        # If you think you're highest, return an array where the first element is the
        # phrase "Zip Deck!", and the second is a dictionary for how you'd assign points
        # if you win.
        # E.g. ["Zip Deck!", {0: 2, 1: 2, 4: 1}]

        # If you don't think you're highest, return an array with one element, the empty
        # string (or anything that's not "Zip Deck!")

        return [""]

class Rando(Player):
    def __init__(self, my_num, player_count):
        super(Rando, self).__init__(my_num, player_count)
    def play(self, card, info):
        if random.random() > 0.5:
            target = {i for i in range(self.player_count)} - {self.my_num}
            target = random.choice(tuple(target))
            points = card//4
            return ["Zip Deck!", {target: points}]
        else:
            return [""]

class Serpentine(Player):
    # Zigs and zags, trying not to do the same thing too many times in a row.
    def __init__(self, my_num, player_count):
        super(Serpentine, self).__init__(my_num, player_count)
        self.two_back = True
        self.one_back = False
        self.targets = {i for i in range(self.player_count)} - {self.my_num}
    def play(self, card, info):
        if len(self.targets) == 0:
            self.targets = {i for i in range(self.player_count)} - {self.my_num}
        will_call = False
        if self.two_back == self.one_back:
            will_call = not self.two_back
        elif card/(self.player_count*4) > 0.8:
            will_call = True

        self.two_back = self.one_back
        self.one_back = will_call

        if will_call:
            target = self.targets.pop()
            return ["Zip Deck!", {target: card//4}]
        else:
            return [""]

class OrionBot(Player):
    def __init__(self, my_num, player_count):
        super(OrionBot, self).__init__(my_num, player_count)
    def play(self, card, info):

        if card > (self.player_count - 1) * 3.5:
            highest = -1
            for each in info["scores"]:
                if info["scores"][each] > highest and each != self.my_num:
                    target = each
                    points = card//4
            return ["Zip Deck!", {target:points}]

        else: 
            return [""]
