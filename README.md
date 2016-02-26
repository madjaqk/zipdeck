## Zip Deck rules:

There are N players, and a deck with N*4 cards.  The deck is shuffled (Python's random.shuffle function) and each player is dealt a card.  Everyone looks at their card, then, on the count of three, if you believe you have the highest card, say (return) "Zip Deck!"

If you *do* have the highest card and you said "Zip Deck", you win!  You assign floor[C/4] points, divided between the other players any way you'd like, where C is the value of your card.

If either you said "Zip Deck" but *don't* have the high card, or you do have the high card but *didn't* say "Zip Deck", you take a penalty of floor[C/4] points.

The winner is the player with the fewest total points after a set number of rounds (as of now, N<sup>2</sup> rounds).

## What You Do:

Write a bot!  A bot is a descendant of the Player class.  Your bot should have a function ```play``` that takes two parameters, card (the card your dealt) and info (a dictionary with information about the state of the game).  If your bot thinks it has the highest card, it should return an array containing the string "Zip Deck!" and a dictionary showing how it would assign points if it's correct.  If you don't assign enough points, your bot will take the remainder; if you assign too many, instead all of the points will be given to your bot that round.

Every Player also has two attributes that you can access, ```my_num``` (that player's number) and ```player_count``` (the total number of players).

```python
class YourBotHere(Player):
    def __init__(self, my_num, player_count):
        super(YourBotHere, self).__init__(my_num, player_count)
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
```

```python
class Player(object):
    def __init__(self, my_num, player_count):
        self.my_num = my_num
        self.player_count = player_count
```

Example bots:

```python
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
```

```python
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
```
