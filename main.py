from api.Game import Game
from game.states.LevelState import LevelState

# ================== Punto de entrada del programa. ====================

g = Game()
initState = LevelState()

g.setState(initState)

g.gameLoop()
g.destroy()