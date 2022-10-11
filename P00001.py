import random

from RPSLS_player import RPSLS_player

class P00001(RPSLS_player): #plays randomly
  def __init__(self):
    self.cand = ["rock", "paper", "scissors", "lizard", "spock"]

  def shoot(self):
      return self.cand[random.randrange(0, len(self.cand))]
  
  def update(self, result: str, competitor_shot: str):
    pass
