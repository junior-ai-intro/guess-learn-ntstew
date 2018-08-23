import numpy as np

class Maze():
    actions = ['N','S','E','W']
    # offsets to move North, South, East, or West
    offset = [(-1,0),(1,0),(0,1),(0,-1)]
    
    def __init__(self, random=False):   
        self.reset(random)
    
    # moved code from __init__ to here, to allow re-use of Maze instance
    def reset(self, random=False):
        if random:
            self.maze = np.random.randint(0,2,size=(4,4))
            self.maze[0][0] = 0  # no obstacles allowed at starting point...
            self.maze[3][3] = 0  # ...or at ending point.
        else:
            self.maze = np.array([[0,0,0,-1],[0,-1,0,0],[0,0,-1,0],[-1,-1,0,0]])  # the initial maze is hardcoded
        self.i = 1
        self.maze[0][0] = self.i  # initial position
        self.player = np.array([0,0])
        return self.player
    
    # action should be one of: 'N', 'S', 'E', 'W'
    # returns reward, done
    # rewards are: +1 = success, -1 = failure, 0 = no outcome
    # done = True if a terminal state is reached, otherwise False
    def step(self, action):
        self.i += 1
        if type(action) is str:
            action = Maze.actions.index(action)
        self.player = np.add(self.player, Maze.offset[action])
        if max(self.player) > 3 or min(self.player) < 0:        # out of bounds
            return self.player, -1, True
        else:
            if self.maze[self.player[0]][self.player[1]] == -1: # moved onto a blocked space
                return self.player, -1, True
            self.maze[self.player[0]][self.player[1]] = self.i
            if np.array_equal(self.player, (3,3)):              # reached the exit
                return self.player, 1, True
            else:
                return self.player, 0, False                    # no outcome (player is on an open space)
    
    # return a random action (equally distributed across the action space)
    def sample(self):
        return Maze.actions[np.random.randint(4)]
    
    def action_space(self):
        return Maze.actions
    
    def state_space(self):
        return 4,4
    
    def __str__(self):
        out = '===================================\n'
        for row in range(len(self.maze)):
            for line in range(3):
                if row == 0 and line == 1:
                    out += 'enter-> '
                else:
                    out += '        '
                for col in range(len(self.maze)):
                    if self.maze[row][col] == -1:
                        out += ' +++ '
                    elif self.maze[row][col] == 0 or line != 1:
                        out += ' ... '
                    else:
                        out += ' ('
                        out += str(self.maze[row][col])
                        out += ') '
                    if row == len(self.maze)-1 and col == len(self.maze)-1 and line == 1:
                        out += ' <-exit'
                out += '\n'
            out += '\n'
        out += '==================================='
        return out
    
    def print_q(q):
        print('=====  ================================')
        print('state         N       S       E       W\n')
        for m in range(4):
            for n in range(4):
                out = '('
                out += str(m)
                out += ','
                out += str(n)
                out += ')  '
                for a in range(4):
                    out += '{:>8,d}'.format(int(q[m][n][a]))
                print(out)
            print('-----  --------------------------------')
         
                
                
    


