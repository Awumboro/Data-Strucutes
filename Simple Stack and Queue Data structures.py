# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 00:59:23 2021

@author: Kojo Justine
"""

# My implementations of data structures

'''
My data structures implementation of 
1. Stack
2. Queue

using python language

'''

# Stack data structure
'''
Stacks can be implemented in Undo and Redo

Adding: first element comes at the bottom and next element falls at the top

Exiting: The topmost element is first to exit in that order
'''
class Stack:
    def __init__(self):
        self.items = []

    # A method to add items to the stack container
    def push (self, item):
        self.items.append( item)
        
    # A method to remove topmost item from the stack container
    def pop (self):
        self.items.pop()
        
    def is_empty (self): #checking to see if it is empty
        return self.items == []
    
    def show_stack (self): # a customized way of displaying it
        return "\n The stack of elements are {} with length of {}".format(self.items, len(self.items))


# calling the class and adding items to it 
    
s = Stack()
s.push(45)
s.push(230)
s.push(2)

s.push(23)
s.push(89)
s.push(29)
s.pop()
print(s.show_stack())


# ====================================================================================================


# Queue data structure
'''
Stacks can be implemented in a printing machine

Adding: first element comes at the back of the queue and next element falls behind it in that order

Exiting: The first element is first to exit in that order
'''

class Queue:
    def __init__(self):
        self.items = []
        
    # A method to add items to the queued 
    def add_queue(self, item):
        self.items.append(item)
        
    def exit_queue(self): #Removing first item from the queue i.e. exiting
        self.items.pop(0)
        
    def is_empty (self):
        self.items == []
        
    def show_queue(self):
        return "\n The Queue of elements are {} with length of {}".format(self.items, len(self.items))
    

# calling the class and adding items to it 
q = Queue()

q.add_queue(23)
q.add_queue(4)
q.add_queue(645)
q.add_queue(234)
q.add_queue(400)
q.add_queue(640)
q.exit_queue()

print(q.show_queue())


