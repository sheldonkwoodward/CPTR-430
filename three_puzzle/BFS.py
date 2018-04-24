# sheldon woodward
# 4/23/18


class BFS:
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
        BFS.loops = []
        BFS.queue = []
        BFS.queue.append(self)
        print('push: ' + str(BFS.queue[-1]))
        print('      ' + str(BFS.queue))
        while len(BFS.queue) > 0:
            BFS.queue[0].process()

    def process(self):
        # input()
        # check if solved
        if self.state == [1, 2, 3, None]:
            print('SOLUTION FOUND')
        elif self.state in BFS.loops:
            BFS.queue.pop(0)
            return
        else:
            BFS.loops.append(self.state)
        # move up and down
        if self.state.index(None) >= 2:
            new_state = self.state[:]
            i = new_state.index(None)
            new_state[i] = self.state[i - 2]
            new_state[i - 2] = self.state[i]
            if new_state not in BFS.loops:
                BFS.queue.append(BFS(state=new_state[:], depth=self.depth + 1))
                print('push: ' + str(BFS.queue[-1]))
                print('      ' + str(BFS.queue))
        else:
            new_state = self.state[:]
            i = new_state.index(None)
            new_state[i] = self.state[i + 2]
            new_state[i + 2] = self.state[i]
            if new_state not in BFS.loops:
                BFS.queue.append(BFS(state=new_state[:], depth=self.depth + 1))
                print('push: ' + str(BFS.queue[-1]))
                print('      ' + str(BFS.queue))
        # move right and left
        if self.state.index(None) % 2 == 0:
            new_state = self.state[:]
            i = new_state.index(None)
            new_state[i] = self.state[i + 1]
            new_state[i + 1] = self.state[i]
            if new_state not in BFS.loops:
                BFS.queue.append(BFS(state=new_state[:], depth=self.depth + 1))
                print('push: ' + str(BFS.queue[-1]))
                print('      ' + str(BFS.queue))
        else:
            new_state = self.state[:]
            i = new_state.index(None)
            new_state[i] = self.state[i - 1]
            new_state[i - 1] = self.state[i]
            if new_state not in BFS.loops:
                BFS.queue.append(BFS(state=new_state[:], depth=self.depth + 1))
                print('push: ' + str(BFS.queue[-1]))
                print('      ' + str(BFS.queue))
        # pop queue
        print(' pop: ' + str(BFS.queue[0]))
        BFS.queue.pop(0)
        print('      ' + str(BFS.queue))
