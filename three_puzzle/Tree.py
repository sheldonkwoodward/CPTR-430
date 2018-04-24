# sheldon woodward
# 4/23/18

"""Tree with different searches for three_puzzle."""


class Tree:
    loops = []
    queue = []
    iterations = 0
    start_state = [3, 1, 2, None]
    goal_state = [1, 2, 3, None]

    def __init__(self, state=None, depth=0, accum_cost=0, moves=''):
        # increment iterations
        Tree.iterations += 1
        # set current state
        if state is None:
            self.state = Tree.start_state
        else:
            self.state = state
        self.moves = moves
        # tree depth
        self.depth = depth
        # tiles matching goal state
        self.matches = len([i for i, j in zip(self.state[:], Tree.goal_state) if i == j and i is not None])
        # manhattan distance + depth
        self.distance = self.depth
        for t in self.state:
            if self.state is None:
                continue
            self.distance += abs(self.state.index(t) % 2 - Tree.goal_state.index(t) % 2) + \
                             abs(self.state.index(t) / 2 - Tree.goal_state.index(t) / 2)
        # unmatched tiles + depth
        self.cost = 3 - self.matches + depth
        # cost + inherited cost
        self.inherited_cost = self.cost + accum_cost

    def __repr__(self):
        display = self.state[:]
        for i, t in enumerate(display):
            if t is None:
                display[i] = 'N'
        return '\n  ---\n| ' + str(display[0]) + ' ' + str(display[1]) + ' |\n| ' + str(display[2]) + ' ' + str(
            display[3]) + ' |\n  ---\n'

    def bfs_search(self):
        self.reset()
        Tree.queue.append(self)
        while len(Tree.queue) > 0:
            next_tree_index = 0
            result = Tree.queue[next_tree_index].process(next_tree_index)
            if result is not None:
                return result
        return 'No solution'

    def bbpc_search(self):
        self.reset()
        Tree.queue.append(self)
        while len(Tree.queue) > 0:
            next_tree_index = 0
            for i, t in enumerate(Tree.queue[:]):
                if Tree.queue[next_tree_index].depth > t.depth:
                    next_tree_index = i
            result = Tree.queue[next_tree_index].process(next_tree_index)
            if result is not None:
                return result
        return 'No solution'

    def bbsh_search(self):
        self.reset()
        Tree.queue.append(self)
        while len(Tree.queue) > 0:
            next_tree_index = 0
            for i, t in enumerate(Tree.queue[:]):
                if Tree.queue[next_tree_index].cost > t.cost:
                    next_tree_index = i
            result = Tree.queue[next_tree_index].process(next_tree_index)
            if result is not None:
                return result
        return 'No solution'

    def bbrh_search(self):
        self.reset()
        Tree.queue.append(self)
        while len(Tree.queue) > 0:
            next_tree_index = 0
            for i, t in enumerate(Tree.queue[:]):
                if Tree.queue[next_tree_index].inherited_cost > t.inherited_cost:
                    next_tree_index = i
            result = Tree.queue[next_tree_index].process(next_tree_index)
            if result is not None:
                return result
        return 'No solution'

    def a_search(self):
        self.reset()
        Tree.queue.append(self)
        while len(Tree.queue) > 0:
            next_tree_index = 0
            for i, t in enumerate(Tree.queue[:]):
                if Tree.queue[next_tree_index].distance > t.distance:
                    next_tree_index = i
            result = Tree.queue[next_tree_index].process(next_tree_index)
            if result is not None:
                return result
        return 'No solution'

    @staticmethod
    def reset():
        Tree.loops = []
        Tree.queue = []
        Tree.iterations = 0

    def process(self, q_index):
        # check if solved
        if self.state == Tree.goal_state:
            return self.moves
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
            Tree.queue.append(Tree(new_state[:], self.depth + 1, self.inherited_cost, self.moves + 'U'))
        else:
            new_state = self.state[:]
            i = new_state.index(None)
            new_state[i] = self.state[i + 2]
            new_state[i + 2] = self.state[i]
            Tree.queue.append(Tree(new_state[:], self.depth + 1, self.inherited_cost, self.moves + 'D'))
        # move right and left
        if self.state.index(None) % 2 == 0:
            new_state = self.state[:]
            i = new_state.index(None)
            new_state[i] = self.state[i + 1]
            new_state[i + 1] = self.state[i]
            Tree.queue.append(Tree(new_state[:], self.depth + 1, self.inherited_cost, self.moves + 'R'))
        else:
            new_state = self.state[:]
            i = new_state.index(None)
            new_state[i] = self.state[i - 1]
            new_state[i - 1] = self.state[i]
            Tree.queue.append(Tree(new_state[:], self.depth + 1, self.inherited_cost, self.moves + 'L'))
        # pop queue
        Tree.queue.pop(q_index)
        return None
