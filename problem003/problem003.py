'''
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the
tree into a string, and deserialize(s), which deserializes the string back into
the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''    

import json


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.serialized_tree_map = {}

    def __repr__(self):
        return str(self.val)


def serializeNode(node):
    node.serialized_tree_map["val"] = node.val

    if node.left:
        node.serialized_tree_map["left"] = serializeNode(node.left)
    else:
        node.serialized_tree_map["left"] = None

    if node.right:
        node.serialized_tree_map["right"] = serializeNode(node.right)
    else:
        node.serialized_tree_map["right"] = None 
        
    return node.serialized_tree_map

def serialize(node):
    return json.dumps(serializeNode(node))

def deserialize(s):
    deserialized_tree = json.loads(s)
    
    if deserialized_tree["left"] and deserialized_tree["right"]:
        return Node(deserialized_tree["val"], deserialize(json.dumps(deserialized_tree["left"])),\
                    deserialize(json.dumps(deserialized_tree["right"])))
    elif deserialized_tree["left"]:
        return Node(deserialized_tree["val"], deserialize(json.dumps(deserialized_tree["left"])), None)
    elif deserialized_tree["right"]:
        return Node(deserialized_tree["val"], None, deserialize(json.dumps(deserialized_tree["right"])))
    else:
        return Node(deserialized_tree["val"])

# checks:
node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node4 = Node("4")
node5 = Node("5")

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
serialized_node1 = serialize(node1)
#print(serialized_node1)

deserializes_node1 = deserialize(serialized_node1)
#print(deserializes_node1)


nodetest = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(nodetest)).left.left.val == "left.left"
assert deserialize(serialize(nodetest)).right.val == "right"

