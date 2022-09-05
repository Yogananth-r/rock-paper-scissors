# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
rps={}
def player(prev_play, opponent_history=[]):
  global rps
  n=3
  if prev_play in ["R","P","S"]:
    opponent_history.append(prev_play)

  guess = "R"
  if len(opponent_history) > n:
    guess = "".join(opponent_history[-n:])
    if "".join(opponent_history[-(n+1):]) in rps.keys():
      rps["".join(opponent_history[-(n+1):])]+=1
    else:
      rps["".join(opponent_history[-(n+1):])]=1

    pos=[guess+"R",guess+"P",guess+"S"]

    for i in pos:
      if not i in rps.keys():
        rps[i]=0
    pred=max(pos,key=lambda key:rps[key])
    if pred[-1]=="P":
      guess="S"
    if pred[-1]=="R":
      guess="P"
    if pred[-1]=="S":
      guess="R"
    
  return guess
