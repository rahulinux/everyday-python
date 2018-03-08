#!/usr/bin/env python


class Node:
   def __init__(self,value):
     self.value = value
     self.left_child = None
     self.right_child = None


class BinarySearchTree:
   def __init__(self,root=None):
     self.root = None 

   def insert(self,value):
     if self.root == None:
        self.root = Node(value)
     else:
        self._insert(value,self.root)

   def _insert(self,value,current_node):
     if value < current_node.value:
        if current_node.left_child == None:
           current_node.left_child = Node(value)
        else:
           self._insert(value,current_node.left_child)
     elif value > current_node.value:
        if current_node.right_child == None:
           current_node.right_child = Node(value)
        else:
           self._insert(value,current_node.right_child)
     else:
        print "Value already there in tree"


   def print_tree(self):
     if self.root != None:
         self._print_tree(self.root)


   def _print_tree(self,curr_node):
     if curr_node != None:
          self._print_tree(curr_node.left_child)
          print curr_node.value
          self._print_tree(curr_node.right_child)


bt = BinarySearchTree()

bt.insert("a")
bt.insert("b")
bt.insert("c")

bt.print_tree()
