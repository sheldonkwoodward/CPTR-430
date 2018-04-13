# sheldon woodward
# DATE

"""Tree of all farmer-wolf-goat-cabbage possibilities."""

states = []


class Tree:
    def __init__(self, state=[False, False, False, False]):
        # check for loop state
        global states
        states.append(state)
        self.state = state
        self.nodes = []

        # generate next nodes
        for i, s in enumerate(state):
            # generate state
            new_state = state
            new_state[0] = not new_state[0]
            if i > 0:
                new_state[i] = not new_state[i]
            # add to tree
            if not Tree.bad_state(new_state):
                self.nodes.append(Tree(new_state))

    @staticmethod
    def bad_state(state):
        # pre-existing state
        global states
        if state in states:
            return True
        # wolf alone with goat
        if state[0] != state[1] and state[1] == state[2]:
            return True
        # goat alone with cabbage
        if state[0] != state[2] and state[2] == state[3]:
            return True
        return False
