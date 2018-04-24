# sheldon woodward
# 4/23/18


class Tree:
    loops = []
    queue = []
    start_state = [3, 1, 2, None]
    goal_state = [1, 2, 3, None]

    def __init__(self, state=None, depth=0):
        if state is None:
            self.state = Tree.start_state
        else:
            self.state = state
        self.depth = depth
        self.matches = len([i for i, j in zip(self.state[:], Tree.goal_state) if i == j and i is not None])
        self.cost = 3 - self.matches + depth
        self.nodes = []

    def __repr__(self):
        display = self.state[:]
        for i, t in enumerate(display):
            if t is None:
                display[i] = 'N'
        return '\n  ---\n| ' + str(display[0]) + ' ' + str(display[1]) + ' |\n| ' + str(display[2]) + ' ' + str(
            display[3]) + ' |\n  ---\n'

    def search(self, method='bfs'):
        Tree.loops = []
        Tree.queue = []
        Tree.queue.append(self)
        # print('push: ' + str(Tree.queue[-1]))
        # print('   d: ' + str(Tree.queue[-1].depth))
        # print('   m: ' + str(Tree.queue[-1].matches))
        # print('   c: ' + str(Tree.queue[-1].cost))
        # print('   q: ' + str(Tree.queue))
        # print()
        while len(Tree.queue) > 0:
            if method == 'bfs':
                print(' chs: ' + str(Tree.queue[0]))
                Tree.queue[0].process(0)
            elif method == 'bbsh':
                next_tree_index = 0
                for i, t in enumerate(Tree.queue[:]):
                    if Tree.queue[next_tree_index].cost > t.cost:
                        next_tree_index = i
                print(' chs: ' + str(Tree.queue[next_tree_index]))
                # print('   d: ' + str(Tree.queue[next_tree_index].depth))
                # print('   m: ' + str(Tree.queue[next_tree_index].matches))
                # print('   c: ' + str(Tree.queue[next_tree_index].cost))
                Tree.queue[next_tree_index].process(next_tree_index)

    def process(self, q_index):
        # check if solved
        if self.state == Tree.goal_state:
            print('SOLUTION FOUND')
        elif self.state in Tree.loops:
            Tree.queue.pop(q_index)
            return
        else:
            Tree.loops.append(self.state)
        # move up and down
        if self.state.index(None) >= 2:
            new_state = self.state[:]
            i = new_state.index(None)
            new_state[i] = self.state[i - 2]
            new_state[i - 2] = self.state[i]
            Tree.queue.append(Tree(state=new_state[:], depth=self.depth + 1))
            # print('push: ' + str(Tree.queue[-1]))
            # print('   d: ' + str(Tree.queue[-1].depth))
            # print('   m: ' + str(Tree.queue[-1].matches))
            # print('   c: ' + str(Tree.queue[-1].cost))
            # print('   q: ' + str(Tree.queue))
            # print()
        else:
            new_state = self.state[:]
            i = new_state.index(None)
            new_state[i] = self.state[i + 2]
            new_state[i + 2] = self.state[i]
            Tree.queue.append(Tree(state=new_state[:], depth=self.depth + 1))
            # print('push: ' + str(Tree.queue[-1]))
            # print('   d: ' + str(Tree.queue[-1].depth))
            # print('   m: ' + str(Tree.queue[-1].matches))
            # print('   c: ' + str(Tree.queue[-1].cost))
            # print('   q: ' + str(Tree.queue))
            # print()
        # move right and left
        if self.state.index(None) % 2 == 0:
            new_state = self.state[:]
            i = new_state.index(None)
            new_state[i] = self.state[i + 1]
            new_state[i + 1] = self.state[i]
            Tree.queue.append(Tree(state=new_state[:], depth=self.depth + 1))
            # print('push: ' + str(Tree.queue[-1]))
            # print('   d: ' + str(Tree.queue[-1].depth))
            # print('   m: ' + str(Tree.queue[-1].matches))
            # print('   c: ' + str(Tree.queue[-1].cost))
            # print('   q: ' + str(Tree.queue))
            # print()
        else:
            new_state = self.state[:]
            i = new_state.index(None)
            new_state[i] = self.state[i - 1]
            new_state[i - 1] = self.state[i]
            Tree.queue.append(Tree(state=new_state[:], depth=self.depth + 1))
            # print('push: ' + str(Tree.queue[-1]))
            # print('   d: ' + str(Tree.queue[-1].depth))
            # print('   m: ' + str(Tree.queue[-1].matches))
            # print('   c: ' + str(Tree.queue[-1].cost))
            # print('   q: ' + str(Tree.queue))
            # print()
        # pop queue
        # print(' pop: ' + str(Tree.queue[q_index]))
        Tree.queue.pop(q_index)
        # print('      ' + str(Tree.queue))
        # print('--------------------------------')
