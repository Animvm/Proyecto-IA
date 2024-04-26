from vizdoom import *
from vizdoom import DoomGame
import random
import time
import numpy as np

from gym import Env
from gym.spaces import Discrete, Box
import cv2

game = DoomGame()
game.load_config(".venv/Lib/site-packages/vizdoom/scenarios/basic.cfg")
game.init()

# # Acciones que puede realizar el agente
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

#Creación del ambiente de entrenamiento
# class VizDoomGym(Env):
#     def __init__(self, render=False):
#         super().__init__()
#         self.game = DoomGame()
#         self.game.load_config(".venv/Lib/site-packages/vizdoom/scenarios/basic.cfg")

#         if render == False:
#             self.game.set_window_visible(False)
#         else:
#             self.game.set_window_visible(True)

#         #Inicializa el juego
#         self.game.init()

#         self.observation_space = Box(low=0, high=255, shape=(100, 160, 1), dtype=np.uint8)
#         self.action_space = Discrete(3)

#     def step(self, action):
#         #Especifica las acciones que el agente puede realizar
#         actions = np.identity(3, dtype=np.uint8)
#         reward = self.game.make_action(actions[action], 4)

#         #Obtiene las demás variables 
#         if self.game.get_state():
#             state = self.game.get_state().screen_buffer
#             state = self.grayscale(state)
#             info = self.game.get_state().game_variables
#         else:
#             state = np.zeros(self.observation_space.shape)
#             info = 0

#         done = self.game.is_episode_finished()

#         return state, reward, done, info

#     def render():
#         pass
    
#     def reset(self):
#         self.game.new_episode()     
#         state = self.game.get_state().screen_buffer
#         return self.grayscale(state)

#     def grayscale(self, observation):
#         gray = cv2.cvtColor(np.moveaxis(observation, 0, -1), cv2.COLOR_BGR2GRAY)
#         resize = cv2.resize(gray, (160, 100), interpolation=cv2.INTER_CUBIC)
#         state = np.reshape(resize, (100, 160, 1))
#         return state

#     def close(self):
#         self.game.close()

# env = VizDoomGym(render=True)
# state = env.reset()
# np.moveaxis(state, 0, -1).shape
# env.step(2)
# env.close(