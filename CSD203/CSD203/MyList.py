from Car import *
from Node import *
class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head ==None
    def traverse(self):
        pt = self.head
        while pt:
            print(pt.data, end = " ")
            pt = pt.next
        print("")        
    def clear(self):
        self.head = None
#Q1-1
    def addLast(self, name="", price=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        if name[0] == "B" or price > 100:
            return
        newNode = Node(data = Car(name, price))
        if self.tail == None:
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode


        
    # end def
#Q1-2    
    def addFirst(self, name="", price=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
         newNode = Node(data=Car(name, price))
         if (self.isEmpty()):
             self.head = self.tail = newNode
             return
         else:
             newNode.next = self.head
             self.head = newNode




        
    # end def
#Q1-3
    def delete(self, price =0):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        curr = self.head
        count = 0
        while curr:
            count +=1
            curr = curr.next
        if count < 3:
            return
        if self.head.data.Price == 5:
            self.head = self.head.next
            return
        prev = self.head
        curr = prev.next
        while curr:
            if curr.data.Price == 5:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
        pass 
    #end def
# Q1-4
    def sort(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        if self.head is None:
            return
        current = self.head
        while current.next:
            if current.data.Price > current.next.data.Price:
                current.data.Name, current.next.data.Name = current.next.data.Name, current.data.Name
                current.data.Price, current.next.data.Price = current.next.data.Price, current.data.Price
                current = self.head
            else:
                current = current.next
        
        

        
        pass
    #end def    