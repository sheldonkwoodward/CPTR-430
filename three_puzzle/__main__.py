# sheldon woodward
# 4/23/18

"""Main function for three_puzzle problem."""

from three_puzzle import Tree


def main(args=None):
    t = Tree()
    t.search(method='bbpc')


if __name__ == '__main__':
    main()
