"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __str__(self):
        out = ""
        # Add head to string
        if self.head:
            out += f"{self.head.value} -> "
        else:
            return "empty list"
        # loop from head+1 to tail
        next = self.head.next
        while next:
            out += f"{next.value} -> "
            next = next.next
        return out[:-4]

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        pass
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head:
            # Head present, save for return
            removedHead = self.head

            if self.head.next:
                # More than one node in list, set head to self.head.next and remove new heads prev
                self.head = self.head.next
                self.head.prev = None
            else:
                # Head is only node in list, set head and tail to None
                self.head = None
                self.tail = None
            
            # Return the removed value
            return removedHead.value

        # No head present, ret None
        return None
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        newNode = ListNode(value)
        if self.tail:
            # If we are adding the second item in the list, we need to add based on self.head instead of the tail so that we can link everything correctly
            if self.head.next == None:
                # Add node to head
                newNode.prev = self.head
                self.head.next = newNode
            else:
                # Add node to tail
                newNode.prev = self.tail
                self.tail.next = newNode
        else:
            # Nothing in list, set the head and tail to the node but do not link them together, as they are technically a single node
            self.head = newNode

        # Always set the tail to the node we added
        self.tail = newNode
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail:
            # Tail present
            # Save old tail for return
            removedTail = self.tail

            if self.tail.prev:
                # More than one node in list
                # .prev is the new tail
                self.tail = self.tail.prev 
                self.tail.next = None

            else:
                # Only one node in list, remove head and tail as they are the same node
                self.head = None
                self.tail = None

            # Return the removed value
            return removedTail.value
                
        # Empty list, nothing to remove
        return None
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass
