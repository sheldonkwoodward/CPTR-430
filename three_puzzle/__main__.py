# sheldon woodward
# 4/23/18

"""Main function for three_puzzle problem."""

from three_puzzle import Tree


def main(args=None):
    t = Tree()
    print('Breadth First Search')
    print('--------------------')
    print('      Path: ' + t.bfs_search())
    print('Iterations: ' + str(t.iterations))
    print()

    print('B&B (past cost)')
    print('---------------')
    print('      Path: ' + t.bbpc_search())
    print('Iterations: ' + str(t.iterations))
    print()

    print('B&B (simple heuristic)')
    print('----------------------')
    print('      Path: ' + t.bbsh_search())
    print('Iterations: ' + str(t.iterations))
    print()

    print('B&B (refined heuristic)')
    print('-----------------------')
    print('      Path: ' + t.bbrh_search())
    print('Iterations: ' + str(t.iterations))
    print()

    print('A * Search')
    print('----------')
    print('      Path: ' + t.a_search())
    print('Iterations: ' + str(t.iterations))
    print()


if __name__ == '__main__':
    main()
