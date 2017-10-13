#Write a function to find the 2nd largest element in a binary search tree.

# find the right most sub tree
# if it has a right node, 2nd largest will be the tree node
# if it doesn't '

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def print(self, indent=0):
        if self.left:
            self.left.print(indent+1)
        print (" " * indent, self.val)
        if self.right:
            self.right.print(indent+1)


def second_largest_value(tree, second_max=None):
    print ("SLV called with")
    tree.print()
    sl = None
    if tree == None:
        return None
    elif tree.right == None and tree.left == None:
        return None
    elif tree.right == None and tree.left != None:
        return tree.left.val

    if tree.right != None:
        sl = second_largest_value(tree.right)
        if sl != None:
            return sl
        elif sl == None:
            return tree.val
    else:
        return sl


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")
i = Node("i")
j = Node("j")
k = Node("k")
l = Node("l")



a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.left = f
# c.right = g
# g.right = h
# h.right = k


print (second_largest_value(a))

# tree = Node(6)
# tree.left = Node(5)
# tree.right = Node(9)
# tree.right.left = Node(8)
# tree.right.right = Node(11)
#
# print (reverse_order_for_second_largest(tree))
#
# tree2 = Node(6)
# tree2.left = Node(5)
# print (reverse_order_for_second_largest(tree2))
