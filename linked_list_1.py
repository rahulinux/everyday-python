#!/usr/local/env python



class Node():
   def __init__(self,data=None):
      self.data = data
      self.next = None



class Linked_List():

   def __init__(self):
      self.head = Node()

   def append(self,data):
      new_node = Node(data)
      curr = self.head
      while curr.next!=None:
          curr = curr.next
      curr.next = new_node

   def delete(self,data):
      curr = self.head
      while curr.next!=None:
           curr = curr.next
           if curr.data == data:
              curr.data = curr.next.data
              curr.next = curr.next.next

   def display(self):
      curr_node = self.head
      temp = []
      while curr_node.next!=None:
           curr_node = curr_node.next
           temp.append(curr_node.data)
      print temp



mylist = Linked_List()
mylist.display()
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.display()
mylist.delete(2)
mylist.display()
