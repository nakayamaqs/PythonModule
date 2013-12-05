#
# Build trees
# From: http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap20.html

class Tree:

    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

class TreeHelper:
    """ Helper class to handle with Tree's cargo """
    def total(tree):
        if tree == None:
            return 0
        return TreeHelper.total(tree.left) + TreeHelper.total(tree.right) + tree.cargo

    def printPreOrder(tree):
        if tree == None:
            return
        print(tree.cargo)
        TreeHelper.printPreOrder(tree.left)
        TreeHelper.printPreOrder(tree.right)

    def printInOrder(tree):
        if tree == None:
            return
        TreeHelper.printPreOrder(tree.left)
        print(tree.cargo)
        TreeHelper.printPreOrder(tree.right)

    def printPostOrder(tree):
        if tree == None:
            return
        TreeHelper.printPreOrder(tree.left)
        TreeHelper.printPreOrder(tree.right)
        print(tree.cargo)

    # Generate a graphical representation of a tree
    def printTreeIndented(tree, level):
        if tree == None: return
        TreeHelper.printTreeIndented(tree.right, level + 1)
        print('  ' * level + '  ' + str(tree.cargo))
        TreeHelper.printTreeIndented(tree.left, level + 1)

    # Generate a graphical representation of a tree with parenthesis
    def printTreeWithPare(tree, level, withPare):
        if tree == None: return
        if withPare and tree.left != None and tree.right != None:
            print('(')
        TreeHelper.printTreeWithPare(tree.right, level + 1, not withPare)
        print('  ' * level + '  ' + str(tree.cargo))
        TreeHelper.printTreeWithPare(tree.left, level + 1, not withPare)
        if withPare and tree.left != None and tree.right != None:
            print(')')


left = Tree(20)
right = Tree(3)
tree = Tree(1, left, right);

print("Info: Total of tree is {total} ".format(total=TreeHelper.total(tree)))
# TreeHelper.printPreOrder(tree)
# TreeHelper.printInOrder(tree)
# TreeHelper.printPostOrder(tree)

# tree traversal
tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))
TreeHelper.printPreOrder(tree)

TreeHelper.printTreeIndented(tree, 0)

tree = Tree('*', Tree(9), Tree('+', Tree(7), Tree(3)))
TreeHelper.printTreeWithPare(tree, 0, False)

