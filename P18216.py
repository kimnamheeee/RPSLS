from RPSLS_player import RPSLS_player
import random
from collections import Counter

class P18216(RPSLS_player):
  def __init__(self):
    self.round = 0
    self.cand = ["rock", "paper", "scissors", "spock", "lizard"]
    self.hist = []

  def shoot(self):
    self.round += 1
    if self.round < 3:
      self.hist.append([self.cand.index("lizard")])
      return "lizard"
    else:
      self.hist.append([self.cand.index(self.selection)])
      return self.selection


  def update(self, result: str, competitor_shot: str):
    self.hist[self.round - 1].append(self.cand.index(competitor_shot))

    self.shot = []

    for i in range(1, len(self.hist)):
      if i == 1:
        self.target = self.hist[-1]
        for j in range(len(self.hist) - 1):
          if self.hist[j] == self.target:
            self.shot.append(j)
      if i == 2:
        if len(self.shot) <= 1:
          break
        else:
          self.target = self.hist[-2]
          for j in self.shot:
            if j == 0:
              pass
            else:
              if self.hist[j - 1] != self.target:
                self.shot[self.shot.index(j)] = ''
                self.rm_set = {''}
                self.shot = [i for i in self.shot if i not in self.rm_set]
      if i >=3:
        if len(self.shot) <= 1:
          break
        else:
          self.test = []
          self.target = self.hist[-i]
          for j in self.shot:
            self.test.append(j)
          for j in self.shot:
            if j == i - 2:
              pass
            else:
              if self.hist[j - (i - 1)] != self.target:
                self.shot[self.shot.index(j)] = ''
          if set(self.shot) == {''}:
            self.shot = self.test
            break
          else:
            self.rm_set = {''}
            self.shot = [i for i in self.shot if i not in self.rm_set]
    
    if self.shot == []:
      self.selection = self.cand[random.randrange(0, len(self.cand))]
    else:
      self.check = []
      for i in self.shot:
        self.check.append(str(self.hist[i + 1]))
      self.count_freq = Counter(self.check)
      self.max_item = self.count_freq.most_common(n=1)
      self.hint = int(self.max_item[0][0][-2])
      self.selection = self.cand[random.choice([(self.hint + 1) % 5, (self.hint + 3) % 5])]
