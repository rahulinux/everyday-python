#!/usr/bin/env python


class Queue:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def enqueue(self,item):
    self.items.insert(0,item)

  def dequeue(self):
    self.items.pop()

  def size(self):
    return len(self.items)


q = Queue()

q.enqueue("Google")
q.enqueue("Facebook")
q.enqueue("Amazon")

print q.size()
