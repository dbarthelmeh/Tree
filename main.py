class Tree(object):
    '''This is a tree.'''
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


root = Tree()  # define a small tree with 5 nodes
root.data = 2
root.left = Tree()
root.right = 4

root.left.data = 3
root.left.left = 5
root.left.right = 6


def find_sum(start):
    '''This function adds up all of the nodes in a tree'''
    if type(start) is int:  # without this we get an attribute error because integers do not have .data
        return start
    elif start.data is None:
        return 0
    else:
        return start.data + find_sum(start.left) + find_sum(start.right)


print(find_sum(root))

