class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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

    
    def add_to_tail(self, value):
        newNode = ListNode(value)
        if self.tail:
            # If we are adding the second item in the list, we need to add based on self.head instead of the tail so that we can link everything correctly
            if self.head.next == None:
                # Add node to head
                self.head.next = newNode
            else:
                # Add node to tail
                self.tail.next = newNode
        else:
            # Nothing in list, set the head and tail to the node but do not link them together, as they are technically a single node
            self.head = newNode

        # Always set the tail to the node we added
        self.tail = newNode

    def remove_head(self):
        if self.head:
            # Head present, save for return
            removedHead = self.head

            if self.head.next:
                # More than one node in list, set head to self.head.next and remove new heads prev
                self.head = self.head.next
            else:
                # Head is only node in list, set head and tail to None
                self.head = None
                self.tail = None
            
            # Return the removed value
            return removedHead.value

        # No head present, ret None
        return None

    def remove_tail(self):
        if self.tail:
            # Tail present
            # Save old tail for return
            removedTail = self.tail

            if self.head.next == None:
                # Only one node in list, remove head and tail as they are the same node
                self.head = None
                self.tail = None
            else:
                # Multiple Nodes in list, need to find the new tail, then remove the current tail
                node = self.head

                # Find second-to-last node
                while hasattr(node.next, 'next') and node.next.next != None:
                    node = node.next
                
                # Remove current tail and set second-to-last node to the new tail
                node.next = None
                self.tail = node

            # Return the removed value
            return removedTail.value
                
        # Empty list, nothing to remove
        return None
