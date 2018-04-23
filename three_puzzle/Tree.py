# sheldon woodward
# 4/23/18


class Tree:
    loops = []
    queue = []

    def __init__(self, state=None, depth=0):
        if state is None:
            self.state = [3, 1, 2, None]
        else:
            self.state = state
        self.depth = depth
        self.nodes = []

    def __repr__(self):
        return str(self.state)

    def bfs(self):
        Tree.loops = []
        Tree.queue = []
        Tree.queue.append(self)
        print('push: ' + str(Tree.queue[-1]))
        print('      ' + str(Tree.queue))
        while len(Tree.queue) > 0:
            Tree.queue[0].process()

    def process(self):
        input()
        # check if solved
        if self.state == [1, 2, 3, None]:
            print('solution found')
        else:
            Tree.loops.append(self.state)
        # move up and down
        if self.state.index(None) >= 2:
            new_state = self.state[:]
            i = new_state.index(None)
            new_state[i] = self.state[i - 2]
            new_state[i - 2] = self.state[i]
            if new_state not in Tree.loops:
                Tree.queue.append(Tree(state=new_state[:], depth=self.depth+1))
                print('push: ' + str(Tree.queue[-1]))
                print('      ' + str(Tree.queue))
        else:
            new_state = self.state[:]
            i = new_state.index(None)
            new_state[i] = self.state[i + 2]
            new_state[i + 2] = self.state[i]
            if new_state not in Tree.loops:
                Tree.queue.append(Tree(state=new_state[:], depth=self.depth+1))
                print('push: ' + str(Tree.queue[-1]))
                print('      ' + str(Tree.queue))
        # move right and left
        if self.state.index(None) % 2 == 0:
            new_state = self.state[:]
            i = new_state.index(None)
            new_state[i] = self.state[i + 1]
            new_state[i + 1] = self.state[i]
            if new_state not in Tree.loops:
                Tree.queue.append(Tree(state=new_state[:], depth=self.depth+1))
                print('push: ' + str(Tree.queue[-1]))
                print('      ' + str(Tree.queue))
        else:
            new_state = self.state[:]
            i = new_state.index(None)
            new_state[i] = self.state[i - 1]
            new_state[i - 1] = self.state[i]
            if new_state not in Tree.loops:
                Tree.queue.append(Tree(state=new_state[:], depth=self.depth+1))
                print('push: ' + str(Tree.queue[-1]))
                print('      ' + str(Tree.queue))
        # pop queue
        print(' pop: ' + str(Tree.queue[0]))
        Tree.queue.pop(0)
        print('      ' + str(Tree.queue))
