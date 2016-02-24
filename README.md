## Zip Deck rules:

There are N players, and a deck with N*4 cards.  The deck is shuffled (Python's random.shuffle function) and each player is dealt a card.  Everyone looks at their card, then, on the count of three, if you believe you have the highest card, say (return) "Zip Deck!"

If you *do* have the highest card and you said "Zip Deck", you win!  You assign floor[C/4] points, divided between the other players any way you'd like, where C is the value of your card.

If either you said "Zip Deck" but *don't* have the high card, or you do have the high card but *didn't* say "Zip Deck", you take a penalty of floor[C/4] points.

The winner is the player with the fewest total points after a set number of rounds (as of now, N<sup>2</sup> rounds).

## What You Do:

Write a bot!  A bot is a descendant of the Player class.

```python
class Player(object):
    def __init__(self, player_num):
        self.player_num = player_num
    def play(self, card, info):
        # Info is a hash containing the number of players, the round number,
        # and every player's score
        # Ex: info = {"player_count": 4, "round": 2, "scores": {0: 2, 1: 0,
        # 2: 2, 3: 6, 4: 5} }

        # Define your own play function for your class.

        # If you think you're highest, return an array where the first
        # element is the phrase "Zip Deck!", and the second is a dictionary 
        # for how you'd assign points if you win.
        # E.g. ["Zip Deck!", {0: 2, 1: 2, 4: 1}]

        # If you don't think you're highest, return an array with one
        # element, the empty string (or anything that's not "Zip Deck!")

        return [""]
```

Example class that plays completely randomly:

```python
class Rando(Player):
    def play(self, card, info):
        if random.random() > 0.5:
            target = {i for i in range(info["player_count"])} 
            target = target - {self.player_num}
            target = random.choice(tuple(target))
            points = card//4
            return ["Zip Deck!", {target: points}]
        else:
            return [""]
```