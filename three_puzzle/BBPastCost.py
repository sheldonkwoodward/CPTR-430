# sheldon woodward
# 4/23/18


class BBPastCost:
    loops = []
    queue = []
    start_state = [3, 1, 2, None]
    goal_state = [1, 2, 3, None]

    def __init__(self, state=None, depth=0):
        if state is None:
            self.state = BBPastCost.start_state
        else:
            self.state = state
        self.depth = depth
        self.matches = len([i for i, j in zip(self.state[:], BBPastCost.goal_state) if i == j and i is not None])
        self.cost = 3 - self.matches + depth
        self.nodes = []

    def __repr__(self):
        display = self.state[:]
        for i, t in enumerate(display):
            if t is None:
                display[i] = 'N'
        return '\n  ---\n| ' + str(display[0]) + ' ' + str(display[1]) + ' |\n| ' + str(display[2]) + ' ' + str(
            display[3]) + ' |\n  ---\n'

    def search(self):
        BBPastCost.loops = []
        BBPastCost.queue = []
        BBPastCost.queue.append(self)
        # print('push: ' + str(BBPastCost.queue[-1]))
        # print('   d: ' + str(BBPastCost.queue[-1].depth))
        # print('   m: ' + str(BBPastCost.queue[-1].matches))
        # print('   c: ' + str(BBPastCost.queue[-1].cost))
        # print('   q: ' + str(BBPastCost.queue))
        print()
        while len(BBPastCost.queue) > 0:
            next_tree_index = 0
            for i, t in enumerate(BBPastCost.queue[:]):
                if BBPastCost.queue[next_tree_index].cost > t.cost:
                    next_tree_index = i
            print(' chs: ' + str(BBPastCost.queue[next_tree_index]))
            # print('   d: ' + str(BBPastCost.queue[next_tree_index].depth))
            # print('   m: ' + str(BBPastCost.queue[next_tree_index].matches))
            # print('   c: ' + str(BBPastCost.queue[next_tree_index].cost))
            BBPastCost.queue[next_tree_index].process(next_tree_index)

    def process(self, q_index):
        input()
        # check if solved
        if self.state == BBPastCost.goal_state:
            print('SOLUTION FOUND')
        elif self.state in BBPastCost.loops:
            BBPastCost.queue.pop(q_index)
            return
        else:
            BBPastCost.loops.append(self.state)
        # move up and down
        if self.state.index(None) >= 2:
            new_state = self.state[:]
            i = new_state.index(None)
            new_state[i] = self.state[i - 2]
            new_state[i - 2] = self.state[i]
            BBPastCost.queue.append(BBPastCost(state=new_state[:], depth=self.depth + 1))
            # print('push: ' + str(BBPastCost.queue[-1]))
            # print('   d: ' + str(BBPastCost.queue[-1].depth))
            # print('   m: ' + str(BBPastCost.queue[-1].matches))
            # print('   c: ' + str(BBPastCost.queue[-1].cost))
            # print('   q: ' + str(BBPastCost.queue))
            # print()
        else:
            new_state = self.state[:]
            i = new_state.index(None)
            new_state[i] = self.state[i + 2]
            new_state[i + 2] = self.state[i]
            BBPastCost.queue.append(BBPastCost(state=new_state[:], depth=self.depth + 1))
            # print('push: ' + str(BBPastCost.queue[-1]))
            # print('   d: ' + str(BBPastCost.queue[-1].depth))
            # print('   m: ' + str(BBPastCost.queue[-1].matches))
            # print('   c: ' + str(BBPastCost.queue[-1].cost))
            # print('   q: ' + str(BBPastCost.queue))
            # print()
        # move right and left
        if self.state.index(None) % 2 == 0:
            new_state = self.state[:]
            i = new_state.index(None)
            new_state[i] = self.state[i + 1]
            new_state[i + 1] = self.state[i]
            BBPastCost.queue.append(BBPastCost(state=new_state[:], depth=self.depth + 1))
            # print('push: ' + str(BBPastCost.queue[-1]))
            # print('   d: ' + str(BBPastCost.queue[-1].depth))
            # print('   m: ' + str(BBPastCost.queue[-1].matches))
            # print('   c: ' + str(BBPastCost.queue[-1].cost))
            # print('   q: ' + str(BBPastCost.queue))
            # print()
        else:
            new_state = self.state[:]
            i = new_state.index(None)
            new_state[i] = self.state[i - 1]
            new_state[i - 1] = self.state[i]
            BBPastCost.queue.append(BBPastCost(state=new_state[:], depth=self.depth + 1))
            # print('push: ' + str(BBPastCost.queue[-1]))
            # print('   d: ' + str(BBPastCost.queue[-1].depth))
            # print('   m: ' + str(BBPastCost.queue[-1].matches))
            # print('   c: ' + str(BBPastCost.queue[-1].cost))
            # print('   q: ' + str(BBPastCost.queue))
            # print()
        # pop queue
        # print(' pop: ' + str(BBPastCost.queue[q_index]))
        BBPastCost.queue.pop(q_index)
        # print('      ' + str(BBPastCost.queue))
        # print('--------------------------------')
