#!/usr/bin/env python 


class Stack:
   def __init__(self):
      self.items = []

   def isEmpty(self):
      if self.items == []:
         return True
      return False

   # Last In First Out
   def push(self,item):
      self.items.insert(0,item)

   def pop(self):
      self.items.pop(0)

   def size(self):
      return len(self.items)

   def peek(self):
      return self.items[0]

   def display(self):
      return self.items

s = Stack()

print s.isEmpty()

s.push(1)
s.push(2)
print s.display()
s.pop()
print s.display()
s.push(3)
s.push(4)
print s.peek()
print s.size()
print s.display()

ss = Stack()

ss.push('x')
ss.push('y')
ss.push('z')

print ss.display()
while not ss.isEmpty():
  ss.pop()
  ss.pop()


print ss.display()
