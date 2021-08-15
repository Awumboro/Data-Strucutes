# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 22:05:03 2021

@author: Awumboro
"""


class Node: #defining what a node is
    data = None
    next_node = None


    def __init__(self, data):
        self.data = data



class LinkedList: #Defining the linked list class

    def __init__(self):
        self.head = None
        self.tail = None
        self.nodes = list()


    def is_empty (self): # checks if the list is empty
        return self.head is None

    def size (self): #determines the size of the list
        counter = 0
        current = self.head

        while current != None: #loopin through list while it has elements
            counter  +=1
            current  = current.next_node

            if current is None:
                break
        return counter

    def append(self, value): #adds to the right of the list
        new_node = Node(value)


        if self.head is None: #in the case where the list is empty
            self.head = new_node
            self.tail = new_node
            self.nodes.append(str(self.head.data))

        elif self.size() > 0: #for the case where list is not empty

            current = self.tail

            while self.size() > 0:
                if current.next_node == None:
                    current.next_node = new_node
                    self.nodes.append(str(current.next_node.data))
                    self.tail = current.next_node

                break

    def prepend(self, value): #adds to the start of the list
        new_node = Node(value)

        if self.head is None: #in the case where the list is empty
            self.head = new_node
            self.tail = new_node
            self.nodes.insert(0,str(self.head.data))

        elif self.size() > 0: #for the case where list is not empty

            new_node.next_node = self.head
            self.head = new_node
            self.nodes.insert(0,str(self.head.data))



    def find(self, key): #searches for a keyword in the list
        current_node = self.head

        while current_node != None:
            if current_node.data == key:
                break
            else: current_node = current_node.next_node


        return "< Value found at Node: %s >" %current_node.data

    def  pop_left(self): #removes the first item on the left/start
        self.head = self.head.next_node
        self.nodes.remove(self.nodes[0])
        return ""

    def pop_right(self): # removes first element on the right / tail
        current_node = self.head

        while current_node != None:

            if current_node.next_node.next_node == None:
                self.tail = current_node
                current_node.next_node = None
                self.nodes.remove(self.nodes[-1])
                break
            else: current_node = current_node.next_node

        return ""


    def __repr__(self): # a customized representation of the list
        return '  ---> '.join(self.nodes)





# ###################################Implementation of a Queue ##################################

class Queue(LinkedList):

    def __init__(self):
        self.head = None
        self.tail = None
        self.nodes = list()

    def add(self, data):
        LinkedList.append(self, data)

    def __repr__(self):


        return '  <--- '.join(self.nodes)




# ###################################Implementation of a Stack ##################################

class Stack(LinkedList):

    def __init__(self):
        self.head = None
        self.tail = None
        self.nodes  = list()

    def add_stack(self,data):
        LinkedList.append(self, data)
        return ''

    def pop(self):
        LinkedList.pop_right(self)
        return ''


    def __repr__(self):


        return '  ---> '.join(self.nodes)





