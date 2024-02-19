# https://medium.com/data-science-in-your-pocket/how-to-create-a-custom-openai-gym-environment-with-codes-fb5de015de3c

import numpy as np
import pygame

import gymnasium as gym
from gymnasium import spaces

from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env

class RobotEnv(gym.Env):
    def __init__(self):
        super(RobotEnv, self).__init__()

        # 3 possible actions: 0=left, 1=right, 2=stay
        self.action_space = spaces.Discrete(3)

        # Observation space
        self.observation_space = spaces.Discrete(12)

        self.start_pos = self.observation_space.sample()
        self.goal_pos = self.observation_space.sample()
        self.current_pos = self.start_pos  # starting position is current posiiton of agent

        # self.reward_history = []
        # self.state_history = []

        # Initialize Pygame, setting display size
        pygame.init()
        self.cell_size = 125
        self.screen = pygame.display.set_mode((12 * self.cell_size, 1 * self.cell_size))

    def reset(self, seed=0):
        self.start_pos = self.observation_space.sample()
        self.current_pos = self.start_pos
        # self.current_pos = self.observation_space.sample()
        self.goal_pos = self.observation_space.sample()
        return (self.current_pos, {})

    def step(self, action):
        # Move the agent based on the selected action
        self.previous_pos = self.current_pos

        if action == 0 and self.current_pos-1 > 0:  # Left
            self.current_pos -= 1
        elif action == 1 and self.current_pos+1 < 12:  # Right
            self.current_pos += 1
        else:  # Stay
            pass

        # Reward function
        if np.array_equal(self.current_pos, self.goal_pos) and action == 2:  # self.current_pos, self.goal_pos
            reward = 10.0
            done = True
        # elif action == 2:
        #     reward = -np.abs((self.current_pos) - (self.goal_pos)) / 10
        #     done = False
        # elif np.array_equal(self.current_pos, self.goal_pos):
        #     reward = 1
        #     done = False
        else:
            if (self.current_pos >= self.start_pos and self.current_pos <= self.goal_pos) or (self.current_pos <= self.start_pos and self.current_pos >= self.goal_pos):
                reward = -np.abs((self.current_pos) - (self.goal_pos))/10
                done = False
            else:
                reward = -np.abs((self.current_pos) - (self.goal_pos))
                done = False

        # # Reward function
        # if np.array_equal(self.previous_pos, self.goal_pos) and action==2: #self.current_pos, self.goal_pos
        #     reward = 10.0
        #     done = True
        # # elif np.array_equal(self.current_pos, self.previous_pos):
        # #     reward = -0.5
        # #     done = False
        # else:
        #     if np.abs((self.current_pos) - (self.goal_pos)) == 0:
        #         reward = 1
        #         done = False
        #     else:
        #         reward = -np.abs((self.current_pos) - (self.goal_pos))/10
        #         done = False

        return self.current_pos, reward, done, False, {}


    def render(self):
        # Clear the screen
        self.screen.fill((255, 255, 255))

        # Draw env elements one cell at a time
        for row in range(1):
            for col in range(12):
                cell_left = col * self.cell_size
                cell_top = row * self.cell_size

                if col == self.start_pos:  # Starting position
                    pygame.draw.rect(self.screen, (0, 255, 0), (cell_left, cell_top, self.cell_size, self.cell_size))
                elif col == self.goal_pos:  # Goal position
                    pygame.draw.rect(self.screen, (255, 0, 0), (cell_left, cell_top, self.cell_size, self.cell_size))

                if col == self.current_pos:  # Agent position
                    pygame.draw.rect(self.screen, (0, 0, 255), (cell_left, cell_top, self.cell_size, self.cell_size))

        pygame.display.update()  # Update the display


# Test the environment
env = RobotEnv()


done = False
while True:
    pygame.event.get()
    action = env.action_space.sample()  # Random action selection
    obs, reward, done, trun, info = env.step(action)
    env.render()
    print('Reward:', reward)
    print('Done:', done)
    if done:
        break

    pygame.time.wait(120)

# Model training
# check_env(env, warn=True)
#
# model = PPO("MlpPolicy", env, verbose=1)
# model.learn(total_timesteps=10240)
# model.save("ppo_rl")

# # Model
# model = PPO.load("ppo_rl.zip")
# obs = env.reset()
# obs = obs[0]
# while True:
#     action, _states = model.predict(obs)
#     obs, rewards, dones, trun, info = env.step(action)
#     print('Reward:', rewards)
#     print('Done:', dones)
#
#     if dones:
#         break
#
#     env.render()
#     pygame.time.wait(100)




