import random
from ZipDeckBots import *

def game(player_functions, rounds=0):
    if rounds==0: rounds = len(player_functions)**2 
    bots = []
    player_count = 0
    scores = {}

    for bot in player_functions:
        bots.append(bot(player_count, len(player_functions)))
        scores[player_count] = 0
        player_count += 1

    deck = [i for i in range(player_count * 4)]

    info = {}
    
    for round_count in range(rounds):
        random.shuffle(deck)
        info["round"] = round_count
        info["scores"] = scores
        
        plays = []
        for bot in bots:
            plays.append(bot.play(deck[bot.my_num], info))
        winner = deck.index(max(deck[:player_count]))

        if plays[winner][0] == "Zip Deck!":
            points_to_assign = deck[winner]//4
            targets = plays[winner][1]
            if sum(targets.values()) > points_to_assign:
                scores[winner] += points_to_assign
            else:
                scores[winner] += max(points_to_assign - sum(targets.values()),0)
                for target in plays[winner][1]:
                    scores[target] += plays[winner][1][target]
        else:
            scores[winner] += max(deck[winner]//4,1)

        for loser in {i for i in range(player_count)} - {winner}:
            if plays[loser][0] == "Zip Deck!":
                scores[loser] += max(deck[loser]//4,1)

        last = {i: [deck[i], plays[i]] for i in range(player_count)}

        info["last"] = last

        print("Player count: {}".format(player_count))
        print(last)
        print(scores)
        print("****************")
            
    for player in range(len(bots)):
        print("Player {}: {} points".format(player, scores[player]))

    return scores

players = [Rando, Rando, Serpentine, Serpentine]

outcome = game(players,4)

print(outcome)

low_score = outcome[min(outcome, key=lambda x: outcome[x])]
print(["{} ({})".format(player, players[player].__name__) for player in outcome if outcome[player] == low_score])
    
