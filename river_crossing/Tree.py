# sheldon woodward
# DATE

"""Tree of all farmer-wolf-goat-cabbage possibilities."""


class Tree:
    states = []

    def __init__(self, depth=0, state=None):
        if state is None:
            state = [False, False, False, False]
        # check for loop state
        Tree.states.append(state)
        self.depth = depth
        self.state = state
        self.nodes = []

        # generate next nodes
        for i in range(4):
            # generate state
            new_state = state[:]
            if i > 0 and new_state[0] == new_state[i]:
                new_state[i] = not new_state[i]
            new_state[0] = not new_state[0]
            # add to tree
            if not Tree.bad_state(new_state):
                self.nodes.append(Tree(depth + 1, new_state))

    @staticmethod
    def bad_state(state):
        # pre-existing state
        if state in Tree.states:
            return True
        # wolf alone with goat
        if state[0] != state[1] and state[1] == state[2]:
            return True
        # goat alone with cabbage
        if state[0] != state[2] and state[2] == state[3]:
            return True
        return False
