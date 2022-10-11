from abc import ABC, abstractmethod

class RPSLS_player(ABC):

  @abstractmethod
  def shoot(self) -> str:
    pass

  # TODO
  # generate shootout of the player
  # update(result, competitor_shot)
  # update last match informations for strategic shootouts

  @abstractmethod
  def update(self, result: str, competitor_shot: str):
    pass