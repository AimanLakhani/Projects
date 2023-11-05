#  File: TestBinaryTree.py

#  Description: functions that extend Binary Tree Class

#  Student Name: Parul Gupta

#  Student UT EID: pg25945 

#  Partner Name: Aiman Lakhani 

#  Partner UT EID: al54554

#  Course Name: CS 313E

#  Unique Number: 58023

#  Date Created: 4/7/2023

#  Date Last Modified: 4/8/2023

import sys

class Node(object):
    def __init__(self, data, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree(object):
    def __init__(self):
        self.root = None

    # insert data into the tree
    def insert(self,data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else: 
            current = self.root
            parent = self.root 
            # if it is less, go to left
            # if it is greater or equal, go to right 
            while current != None: 
                parent = current
                if data < current.data:
                    current = current.lChild
                else:
                    current = current.rChild
            # reached the end 
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node 

    # search for a node within a given data 
    def search_node(self,data):
        current = self.root
        while current != None and current.data != data:
            if data < current.data:
                current = current.lChild
            else:
                current = current.rChild
        return current 

    # inorder traversal - left, center, right
    def in_order(self, aNode):
        if aNode != None:
            self.in_order(aNode.lChild)
            print(aNode.data)
            self.in_order(aNode.rChild)

    # find the node with the minimum value
    def min_node(self):
        # keep going left until you reach the left most 
        # and return that node (it will hold smallest value)
        current = self.root
        parent = self.root
        while current != None:
            parent = current
            current = current.lChild
        return parent 

    # Returns true if two binary trees are similar
    # if nodes have the same key values 
    def is_similar (self, pNode):
        # if root nodes are null for both trees
        if self.root == None and pNode.root == None:
            return True
        # only one of the trees has a null root 
        elif self.root == None or pNode.root == None:
            return False
        return not self.is_diff(self.root, pNode.root)

    # Returns true if 2 binary trees have different node values 
    def is_diff(self, first, second):
        # check if two nodes are equal
        if first.data != second.data:
            return True
        # if both trees have left child 
        if first.lChild != None and second.lChild != None: 
            return(self.is_diff(first.lChild, second.lChild))
        # if one has left child and other doesn't 
        elif first.lChild != second.lChild:
            return True 
        # if both have right child 
        if first.rChild != None and second.rChild != None: 
            return(self.is_diff(first.rChild, second.rChild))
        # if one has right child and other doesn't 
        elif first.rChild != second.rChild:
            return True 

    # Returns a list of nodes at a given level from left to right
    def get_level (self, level): 
        lst = []
        if(self.root == None):
            return lst
        self.get_level_helper(self.root, level, lst)
        return lst 

    # every time move to a child node, subtract level by 1
    def get_level_helper(self, node, level, lst): 
        if level == 0: 
            lst.append(node)
        # if node has a left child
        if node.lChild != None:
            self.get_level_helper(node.lChild, level-1, lst)
        # if node has right child 
        if node.rChild != None: 
            self.get_level_helper(node.rChild, level-1, lst)

    # Returns the height of the tree
    def get_height (self): 
        if self.root == None:
            return 0
        return (self.get_height_helper(self.root, 1))

    # every time we go to child node, increase height by 1
    # return max height 
    def get_height_helper(self, node, level):
        if node.lChild == None and node.rChild == None: 
            return level
        elif node.lChild != None and node.rChild != None: 
            return max(self.get_height_helper(node.lChild, level + 1), self.get_height_helper(node.rChild, level+1))
        elif node.lChild != None: 
            return self.get_height_helper(node.lChild, level+1)
        elif node.rChild != None: 
            return self.get_height_helper(node.rChild, level+1)

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes (self):
        lst = []
        if self.root == None:
            return 0
        self.num_helper(self.root, lst)
        return len(lst)

    # every time a node is visited, add its data to a list 
    def num_helper(self, aNode, lst):
            if aNode != None: 
                lst.append(aNode.data)
            if aNode.lChild != None: 
                self.num_helper(aNode.lChild, lst)
            if aNode.rChild != None:
                self.num_helper(aNode.rChild, lst)

def main():
    # Create three trees - two are the same and the third is different
	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree1_input = list (map (int, line)) 	# converts elements into ints

	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree2_input = list (map (int, line)) 	# converts elements into ints

	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree3_input = list (map (int, line)) 	# converts elements into ints

    # Test your method is_similar()

    # Print the various levels of two of the trees that are different

    # Get the height of the two trees that are different

    # Get the total number of nodes a binary search tree

if __name__ == "__main__":
  main()