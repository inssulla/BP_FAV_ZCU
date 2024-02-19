# https://medium.com/data-science-in-your-pocket/how-to-create-a-custom-openai-gym-environment-with-codes-fb5de015de3c

import numpy as np
import pygame
import random

import pandas as pd

import gymnasium as gym
from gymnasium import spaces


class RobotEnv(gym.Env):
    def __init__(self):
        super(RobotEnv, self).__init__()

        # 3 possible actions: 0=left, 1=right, 2=stay
        self.action_space = spaces.Discrete(3)

        self.zones_number = 24

        # Observation space
        self.observation_space = spaces.Discrete(self.zones_number)

        self.start_pos = self.observation_space.sample()
        self.goal_pos = self.observation_space.sample()
        self.current_pos = self.start_pos  # starting position is current posiiton of agent



        self.state_space = np.zeros([self.zones_number * self.zones_number, 3])
        state = 0
        for start in range(self.zones_number):
            for goal in range(self.zones_number):
                self.state_space[state][0] = state
                self.state_space[state][1] = start
                self.state_space[state][2] = goal
                state += 1


        # Initialize Pygame, setting display size
        # pygame.init()
        self.cell_size = 125
        # self.screen = pygame.display.set_mode((self.zones_number * self.cell_size, 1 * self.cell_size))

    def reset(self, seed=0):
        self.start_pos = self.observation_space.sample()
        self.current_pos = self.start_pos
        # self.current_pos = self.observation_space.sample()
        self.goal_pos = self.observation_space.sample()
        state = env.select_state()
        return state

    def set(self, start, goal):
        self.start_pos = start
        self.current_pos = self.start_pos
        # self.current_pos = self.observation_space.sample()
        self.goal_pos = goal
        state = env.select_state()
        return state

    def step(self, action):
        # Move the agent based on the selected action
        self.previous_pos = self.current_pos

        if action == 0 and self.current_pos-1 >= 0:  # Left
            self.current_pos -= 1
        elif action == 1 and self.current_pos+1 < self.zones_number:  # Right
            self.current_pos += 1
        else:  # Stay
            pass

        # Reward function
        if np.array_equal(self.current_pos, self.goal_pos) and action == 2:  # self.current_pos, self.goal_pos
            reward = 10.0
            done = True
        elif np.array_equal(self.current_pos, self.goal_pos):
            reward = 1
            done = False
        elif action == 2:
            reward = -2
            done = False
        else:
            reward = -np.abs((self.current_pos) - (self.goal_pos)) / self.zones_number
            done = False


        state = env.select_state()
        return state, reward, done, {}

    def select_state(self):
        start = self.current_pos
        goal = self.goal_pos
        state = int(self.state_space[np.logical_and((self.state_space[:, 1] == start), (self.state_space[:, 2] == goal))][0][0])
        return state


    def render(self):
        # Clear the screen
        self.screen.fill((255, 255, 255))

        # Draw env elements one cell at a time
        for row in range(1):
            for col in range(self.zones_number):
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

# done = False
# while True:
#     pygame.event.get()
#     action = env.action_space.sample()  # Random action selection
#     obs, reward, done, trun, info = env.step(action)
#     env.render()
#     print('Reward:', reward)
#     print('Done:', done)
#     if done:
#         break
#
#     pygame.time.wait(100)


# # Model training Q-table
# q_table = np.zeros([env.zones_number * env.zones_number, env.action_space.n])
#
# n_episodes = 12000
# max_iter_episode = 100
# exploration_proba = 1
# exploration_decreasing_decay = 0.0005 #0.000005
# min_exploration_proba = 0.01
#
# gamma = 0.99
# lr = 0.1
#
# total_rewards_episode = list()
# rewards_per_episode = list()
# exploration_proba_episode = list()
#
# # we iterate over episodes
# for e in range(n_episodes):
#     # we initialize the first state of the episode
#     current_state = env.reset()
#     done = False
#
#     # sum the rewards that the agent gets from the environment
#     total_episode_reward = 0
#
#     for i in range(max_iter_episode):
#         # we sample a float from a uniform distribution over 0 and 1
#         # if the sampled flaot is less than the exploration proba
#         #     the agent selects arandom action
#         # else
#         #     he exploits his knowledge using the bellman equation
#
#         if np.random.uniform(0, 1) < exploration_proba:
#             action = env.action_space.sample()
#         else:
#             action = np.argmax(q_table[current_state, :])
#
#         # The environment runs the chosen action and returns
#         # the next state, a reward and true if the epiosed is ended.
#         next_state, reward, done, _ = env.step(action)
#
#         # We update our Q-table using the Q-learning iteration
#         q_table[current_state, action] = (1 - lr) * q_table[current_state, action] + lr * (reward + gamma * max(q_table[next_state, :]))
#         total_episode_reward = total_episode_reward + reward
#         # If the episode is finished, we leave the for loop
#         if done:
#             break
#         current_state = next_state
#     # We update the exploration proba using exponential decay formula
#     exploration_proba = max(min_exploration_proba, np.exp(-exploration_decreasing_decay * e))
#     rewards_per_episode.append(total_episode_reward)
#     exploration_proba_episode.append(exploration_proba)
#
#     print(e, exploration_proba)


# print("Mean reward per thousand episodes")
# for i in range(100):
#     print(f"{(i+1)*100}: mean espiode reward: {np.mean(rewards_per_episode[100*i:100*(i+1)])}")

# DF = pd.DataFrame(rewards_per_episode)
# DF.to_csv('rewards_per_episode15degree.csv', index=False)
#
# DF = pd.DataFrame(exploration_proba_episode)
# DF.to_csv('exploration_proba15degree.csv', index=False)
#
# DF = pd.DataFrame(q_table)
# DF.to_csv('data15degree.csv', index=False)
# df = pd.read_csv('data15degree.csv', sep=',', header=0)
# table = df.values

df = pd.read_csv('rewards_per_episode15degree.csv', sep=',', header=0)
lst = df.values
#
print("Mean reward per thousand episodes")
parameter = 10
for i in range(int(len(lst)/parameter)):
    print(f"{(i+1)*parameter}: mean espiode reward: {np.mean(lst[parameter*i:parameter*(i+1)])}")


for i in range(1000):
    done = False
    current_state = env.reset()
    # current_state = env.set(0,65)
    while True:
        # pygame.event.get()
        action = np.argmax(table[current_state, :])
        # action = np.argmax(q_table[current_state, :])# Random action selection
        obs, reward, done, info = env.step(action)
        # env.render()
        print('Reward:', reward)
        print('Done:', done)
        if done:
            break
        current_state = obs
        # pygame.time.wait(300)






