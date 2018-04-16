# sheldon woodward
# 4/13/18

"""Main function for river_crossing problem."""

from river_crossing import FWGCTree


def main(args=None):
    print('Answer is a string of characters representing what the farmer brings with him as he goes back and forth '
          'across the river. N for nothing, W for the wolf, G for the goat, and C for the cabbage.')
    print('Using DFS to find solution...')
    FWGCTree()
    print('The solution is: ' + FWGCTree.solution)


if __name__ == '__main__':
    main()
