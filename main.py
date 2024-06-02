import json
import time



# name - self explanatory
# round_qty - it is filled in when the round qty is initially declared
# round_results - after each round, it is updated. The parameters follow this format: (player choice, computer choice, round winner)
# winner - filled in after the last round
#score - filled in after the last round in this format: (rounds player won, rounds computer won)

score001 = {
    "name": "Raul Preciado",
    "round_qty": 3,
    "round_results": [('rock', 'paper', 'lose'), ('rock', 'rock', 'draw'), ('paper', 'rock', 'win')],
    "winner": "Raul Preciado",
    "score": (2, 0)

}

with open('score.json', 'w') as outfile:
    outfile.write(json.dumps(score001))


with open("score.json", "r") as infile:
    log = json.loads(infile.read())
print(log)
