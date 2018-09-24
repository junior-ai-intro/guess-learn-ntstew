import numpy as np
from tictactoe import *

env = Game(o_player=VeryGoodPlayer(),animation=True)

discount = 0.9              # these two variables control how we store rewards or penalties in our
explore = 0.01              # q-table, just like in the lessons about the maze.

#######################################################################################################
#                                                                                                     #
# SUPER IMPORTANT POINT: we don't even need to know the dimensions of the problem (the total number   #
#                        of states of actions... we can ask the environment to tell us those limits)  #
#                                                                                                     #
q = np.zeros((Game.state_space(), Game.action_space()))                                               #
#                                                                                                     #
#######################################################################################################

attempts = 0                # keep track of how many times we have tried to solve the problem
not_yet_trained = True      # and keep trying until we are 'trained', see below

while not_yet_trained:
    total_reward = 0
    attempts += 1
    for n in range(10):                                    # play 10 games, keep track of the total reward
        state = env.reset()
        done = False
        ###############################################################################################
        #                                                                                             #
        # The actual q-learning is exactly like the example with the maze                             #
        #                                                                                             #
        while not done:                                                                               #
            if np.random.random() < explore:                                                          #
                action = env.sample()                                                                 #
            else:                                                                                     #
                action = np.argmax(q[state])                                                          #
            new_state, reward, done = env.step(action)                                                #
            q[state][action] += reward + discount * np.amax(q[new_state])                             #
            state = new_state                                                                         #
        #                                                                                             #
        ###############################################################################################
        total_reward += reward
    not_yet_trained = True if total_reward < 0 else False  # if we never lose in 10 games, we are 'trained'
