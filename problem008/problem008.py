"""
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes
under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
    
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 """
 
 
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
 
def is_unival(root):
    if root is None:
        return True
    if root.left != None and root.left.value != root.value:
        return False
    if root.right != None and root.right.value != root.value:
        return False
    if is_unival(root.right) and is_unival(root.left):
        return True

    return False


def count_unival(root):
    if root is None:
        return 0
    
    if is_unival(root):
        return count_unival(root.left) + count_unival(root.right) + 1
    else:
        return count_unival(root.left) + count_unival(root.right)


node_right_left = Node(1, Node(1), Node(1))
node_right = Node(0, node_right_left, Node(0))
root1 = Node(0, Node(1), node_right)
assert count_unival(root1) == 5

node_left = Node(7, Node(7), Node(7))
node_right_right = Node(4, Node(4), Node(4))
node_right = Node(7, Node(4), node_right_right)
root2 = Node(7, node_left, node_right_right)
assert count_unival(root2) == 6
