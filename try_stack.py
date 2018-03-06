#!/usr/bin/env python 


class Stack:
   def __init__(self):
      self.items = []

   def isEmpty(self):
      return self.items == []

   def push(self,item):
      self.items.append(item)

   def pop(self):
      self.items.pop()

   def size(self):
      return len(self.items)

   def peek(self):
      return self.items[len(self.items)-1]

   def display(self):
      return self.items

s = Stack()

print s.isEmpty()

s.push(1)
s.push(2)
print s.display()
s.pop()
print s.display()
s.push(2222)
print s.peek()
print s.size()
