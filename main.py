N = 10000

from RPSLS_game import RPSLS_game

from P18216 import P18216
from P00001 import P00001

game = RPSLS_game(P18216, P00001)
for i in range(1, N+1):
    print(f"[Round {i}]")
    game.proceed_match()

print(game.get_score())
