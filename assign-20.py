class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    # Add element at beginning
    def add_first(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    # Add element at end
    def add_last(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node

    # Delete first node
    def delete_first(self):
        if self.head is None:
            print("Linkedlist is Empty")
        else:
            self.head=self.head.next

    # Delete last node
    def delete_last(self):
        if self.head is None:
            print("Empty")
            return
        if self.head.next is None:
            self.head=None
            return

        current=self.head
        while current.next.next is not None:
            current=current.next
        current.next=None

    # Delete specific value
    def delete_value(self,data):
        if self.head is None:
            print("Empty")
            return

        if data==self.head.data:
            self.head=self.head.next
            return

        current=self.head
        while current.next is not None:
            if data==current.next.data:
                current.next=current.next.next
                return
            current=current.next

        print("Value not found")

    # NEW FUNCTION 1: Search
    def search(self,value):
        current=self.head
        pos=1
        while current is not None:
            if current.data==value:
                print("Found at position",pos)
                return
            current=current.next
            pos+=1
        print("Not found")

    # NEW FUNCTION 2: Reverse Linked List
    def reverse(self):
        prev=None
        current=self.head

        while current is not None:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node

        self.head=prev

    # NEW FUNCTION 3: Insert at Position
    def insert_position(self,data,pos):
        new_node=Node(data)

        if pos==1:
            new_node.next=self.head
            self.head=new_node
            return

        current=self.head
        for i in range(pos-2):
            if current is None:
                print("Out of bound")
                return
            current=current.next

        new_node.next=current.next
        current.next=new_node

    # Size of linked list
    def size(self):
        count=0
        current=self.head
        while current is not None:
            count+=1
            current=current.next
        return count

    # Display linked list
    def display(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next
        print("None")


# Driver Code
obj=Linkedlist()

obj.add_first(99)
obj.add_first(100)
obj.add_first(88)
obj.add_last(77)
obj.display()
obj.insert_position(55,2)   # new function
obj.delete_value(100)
obj.display()
obj.display()

print("Size:",obj.size())
obj.display()
obj.search(77)
obj.display()
obj.reverse()
print("After Reverse:")
obj.display()