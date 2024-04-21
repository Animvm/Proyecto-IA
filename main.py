from vizdoom import DoomGame
import random
import time
import numpy as np

game = DoomGame()
game.load_config('github/ViZDoom/scenarios/basic.cfg')
game.init()

# Acciones que puede realizar el agente
actions = np.identity(3, dtype=np.uint8)
random.choice(actions)

game.new_episode()
game.is_episode_finished()
game.make_action(random.choice(actions))
episodes = 10
for episode in range(episodes):
    game.new_episode()
    while not game.is_episode_finished():