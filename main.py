from vizdoom import *
from vizdoom import DoomGame
import random
import time
import numpy as np

game = DoomGame()
game.load_config(".venv/Lib/site-packages/vizdoom/scenarios/basic.cfg")
game.init()

# Acciones que puede realizar el agente
actions = np.identity(3, dtype=np.uint8)
random.choice(actions)

game.new_episode()
game.is_episode_finished()
game.make_action(random.choice(actions))
episodes = 10
for episode in range(episodes):
    #Crea una nueva partida
    game.new_episode()
    while not game.is_episode_finished():
        state = game.get_state()
        img = state.screen_buffer
        info = state.game_variables
        reward = game.make_action(random.choice(actions),4)
        print("reward:", reward)
        time.sleep(0.02)
    print("Result:", game.get_total_reward())
    time.sleep(2)
game.close()