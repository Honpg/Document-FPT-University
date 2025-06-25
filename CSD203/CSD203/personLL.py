class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class LinkListed:
    def __init__(self):
        self.head = None
        self.tail = None
#1addLast(xName, xAge) – check if xName has the first letter ‘B’ or xAge < 17 then do nothing, otherwise add new person to the end of the list.
    def addLast(self, xName, xAge):
        if xName[0] == "B" or xAge < 17:
            return
        newNode = Node(data = Person(xName, xAge))
        if self.tail == None:
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
#2 Delete the first node having age = 20
    def delAge20(self):
        curr = self.head
        prev = None
        while curr and curr.data.age != 20:
            prev = curr
            curr = curr.next
        if curr is None:  
            return
        if prev is None:  
            self.head = curr.next
        else:
            prev.next = curr.next
            if curr == self.tail:  
                self.tail = prev
        curr.next = None
#2.1 Delete the second node having age = 20
    def delAge2nd20(self):
        if self.head is None:
            return
        curr = self.head
        prev = None
        count = 0
        while curr:
            if curr.data.age == 20:
                count += 1
                if count == 2: # found second person with age 20
                    if prev is None: # deleting the head node
                        self.head = curr.next
                        curr = None
                        return
                    else:
                        prev.next = curr.next
                        curr = None
                        return
            prev = curr
            curr = curr.next
#6 Delete the last node having age = 20
    def delAgeLast20(self):
        if self.head is None:
            return
        elif self.head == self.tail and self.head.data.age == 20:
            self.head = None
            self.tail = None
        else:
            curr = self.head
            prev = None
            while curr.next:
                if curr.next.data.age == 20:
                    prev = curr
                curr = curr.next
            if prev:
                prev.next = prev.next.next
                if prev.next is None:
                    self.tail = prev
            elif self.head.data.age == 20:
                self.head = self.head.next
            else:
                pass
#3
    def displayFirst5(self):
        curr = self.head
        count = 0
        while curr and count < 5:
            if curr.data.age > 22:
                print(curr.data.name, curr.data.age)
                count += 1
            curr = curr.next
#4 Find max age, 2nd max age, third max age
    def findMaxAge(self):
        if self.head == None:
            return None
        
        maxAge = self.head.data.age
        maxPerson = self.head.data
        
        curr = self.head
        while curr:
            if curr.data.age > maxAge:#Để tìm MIN sửa > thành <
                maxAge = curr.data.age
                maxPerson = curr.data
            curr = curr.next
    
        
        print(f"Name: {maxPerson.name}, Age: {maxAge}")
    def find2ndMaxAge(self):
        self.findithMaxAge(2)
    def find3rdMaxAge(self):
        self.findithMaxAge(3)
    def findithMaxAge(self, i): # Tìm max thứ bao nhiêu thay i bằng bấy nhiêu
        self.sortByAge()
        # self.display()
        curr = self.head
        prev = None
        count = 1
        while curr:
            count += 1 
            prev = curr
            curr = curr.next
            if count == i:
                while prev.data.age == curr.data.age:
                    prev = curr
                    curr = curr.next
                print(curr.data.name, curr.data.age)
                break
            
#5 Sort the list descendingly by age.
    def sortByAge(self):
        swap = False
        while not swap:
            curr = self.head
            swap = True
            while curr.next is not None:
                if curr.data.age < curr.next.data.age: # Thay đổi < or > để thay đổi thứ tự tăng dần hoặc giảm dần (descending or ascending)
                    swap = False
                    curr.data, curr.next.data = curr.next.data, curr.data
                curr = curr.next
#9
    def addIndex(self, name, age, index):
        new_person = Person(name, age)
        
        if not self.head:
            self.head = Node(new_person)
            self.tail = self.head
        elif index == 0:
            self.head = Node(new_person, self.head)
        else:
            node = self.head
            for i in range(index-1):
                node = node.next
                if not node:
                    return
            node.next = Node(new_person, node.next)
            if not node.next.next:
                self.tail = node.next
                
    def swapNodesData(self, node1, node2):
        temp = node1.data
        node1.data = node2.data
        node2.data = temp
    def sortByIndex(self, startIndex, endIndex):
        if self.head is None:
            return
        current = self.head
        for i in range(startIndex):
            if current is None:
                return
            current = current.next
        sorted = False
        while not sorted:
            sorted = True
            node = current
            while node.next is not None and node.next != endIndex:
                if node.data.name > node.next.data.name:
                    self.swapNodesData(node, node.next)
                    sorted = False
                node = node.next
#3
    
    def display(self):
         val = self.head
         while val:
             print(val.data.name, val.data.age)
             val = val.next
             
Name = ["A","B","C","D","E","F","I"]
Age = [23,25,16,23,19,20,24]
person = LinkListed()
for i in range(len(Name)):
    person.addLast(Name[i], Age[i])
# person.delAge2nd20()
# person.delAge20()
# person.delAgeLast20()
# person.addIndex("G", 25, 2)
# person.sortByAge()
person.sortByIndex(0, 2)
# person.display()
# person.findMaxAge()
# person.find2ndMaxAge()
# person.find3rdMaxAge()
# person.displayFirst5()








##Một số kiểu add mở rộng dựa trên các đề pe cũ (thay điều kiện theo đề bài yêu cầu cùng như tên biến khi sử dụng)
#Q1-2-1: addNode(self, name, age) so that Z will be after the first student having age is an even number.
#     def addNodeAfterFirst(self, name="", age=-1):
#         # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ========
#         new_node = Node(data=Student(name, age))
#         if self.head == None:
#             self.head = new_node
#             return
#         cur = self.head
#         while cur.next != None and cur.next.data.Age % 2 == 0:
#             cur = cur.next
#             new_node.next = cur.next
#             cur.next = new_node
#             break

#addNode(self, name, age) so that Z will be after the 2nd student having age is an even number.
#     def addAfter2nd(self, name="", age=-1):
#         new_node = Node(data = Student(name, age))
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             curr_node = self.head
#             prev_node = None
#             even_count = 0
#             while curr_node is not None:
#                 if curr_node.data.Age % 2 == 0:
#                     even_count += 1
#                     if even_count == 2:
#                         new_node.next = curr_node.next
#                         curr_node.next = new_node
#                         break
#                 prev_node = curr_node
#                 curr_node = curr_node.next
#             if curr_node is None and prev_node is not None:
#                 prev_node.next = new_node

# addNode(self, name, age) so that Z will be before the 1st student having age is an even number.
#     def addNodeBeforeFirst(self, name, age):
#         new_node = Node(data = Student(name, age))
        # current = self.head
        # prev = None
        # while current and current.next.data.Age % 2 != 0:
        #     prev = current
        #     current = current.next
        # if not current:
        #     return
        # new_node.next = prev.next
        # prev.next = new_node
        
# addNode(self, name, age) so that Z will be before last student having age is an even number.
# def f2(self, Z):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ========           
            # Traverse the linked list to find the last even-aged node
        # add before the last node
        #new_node = Node(data = Student(name, age))
        #current = self.head
        #prev = None
        #while current:
         #   if current.next.data.Age % 2 != 0:
          #      prev = current
           # current = current.next
        #if not prev:
         #   return
        #new_node.next = prev.next
        #prev.next = new_node