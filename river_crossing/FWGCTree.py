# sheldon woodward
# 4/13/18

"""BBPastCost of all farmer-wolf-goat-cabbage possibilities."""


class FWGCTree:
    states = []
    solution = None

    def __init__(self, depth=0, state=None, history=''):
        self.depth = depth
        self.history = history
        self.nodes = []
        # no state given
        if state is None:
            state = [False, False, False, False]
        # check for solution
        if all(state):
            FWGCTree.solution = history
        # check for loop state
        FWGCTree.states.append(state)
        # generate next nodes
        for i in range(4):
            # generate state
            new_state = state[:]
            if i > 0 and new_state[0] == new_state[i]:
                new_state[i] = not new_state[i]
            new_state[0] = not new_state[0]
            # add to tree
            if not FWGCTree.bad_state(new_state):
                self.nodes.append(FWGCTree(depth + 1, new_state, history + ('N', 'W', 'G', 'C')[i]))

    @staticmethod
    def bad_state(state):
        # pre-existing state
        if state in FWGCTree.states:
            return True
        # wolf alone with goat
        if state[0] != state[1] and state[1] == state[2]:
            return True
        # goat alone with cabbage
        if state[0] != state[2] and state[2] == state[3]:
            return True
        return False
