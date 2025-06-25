class Song:
    def __init__(self, id, name, rating):
        self.id = id
        self.name = name
        self.rating = rating
class Node:
    def __init__(self, info = None, left = None, right = None, parent = None):
        self.info = info
        self.left = left
        self.right = right
        self.parent = parent
class BinaryTree():
    def __init__(self):
        self.root = None
#1 
    def insert(self, xId, xName, xRating):
        newNode = Node(info = Song(xId, xName, xRating))
        if "Paris" in xName.lower() or xRating == 1:
            return
        if self.root is None:
            self.root = newNode
        else:
            current = self.root
            while current:
                if xId < current.info.id:
                    if current.left:
                        current = current.left
                    else:
                        current.left = newNode
                        newNode.parent = current
                        break
                elif xId > current.info.id:
                    if current.right:
                        current = current.right
                    else:
                        current.right = newNode
                        newNode.parent = current
                        break
                else:
                     break
#2
    def dpblanceFactorMoreThan3(self):
        return self.blanceFactorMoreThan3(self.root)
    def blanceFactorMoreThan3(self, root):
        if root is not None:
            self.blanceFactorMoreThan3(root.left)
            self.blanceFactorMoreThan3(root.right)
            balanceFactor = self.balanceFactor(root)
            if balanceFactor <= 3:
                print(f"{root.info.id} | {root.info.name} | {root.info.rating} | {balanceFactor}")
    def balanceFactor(self, root):
        rightHeight = self.height(root.right)
        leftHeight = self.height(root.left)
        return rightHeight - leftHeight

    def height(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))
#3
    def Q3(self):
        self.inVisit()
        p = self.search_f3()
        self.delByMergingLeft(p)
        print("After delete")
        self.inVisit()
    def search_f3(self):
        lst = []
        lst.append(self.root)
        count = 0
        while len(lst) != 0:
            p = lst.pop()
            if p is not self.root and p.info.rating >= 3:
            #Sửa điều kiện theo yêu cầu đề bài
                count += 1
            if count == 2:
            # Đề yêu cầu là node thứ mấy thì count bằng bấy nhiêu (ví dụ đề yêu cầu 'first node' thì count = 1
                return p
            if p.left!=None:
                lst.append(p.left)
            if p.right!=None:
                lst.append(p.right)
        return None
    def delByMergingLeft(self, p):
        parent = None
        node = self.root
        while node and node != p:
            parent = node
            if node.info.rating < p.info.rating:
                node = node.right
            else:
                node = node.left
        if not node:
            return
        # Ko có con
        if not node.left and not node.right:
            if parent:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None
            del node
            return
        # 1 con
        if not node.left:
            child = node.right
        elif not node.right:
            child = node.left
        else:
            # 2 con
            rightMostParent = node
            rightMost = node.left
            while rightMost.right:
                rightMostParent = rightMost
                rightMost = rightMost.right
            node.data = rightMost.data
            node = rightMost
            parent = rightMostParent
            child = rightMost.left
        # Delete the node by merging its child with its parent
        if parent:
            if parent.left == node:
                parent.left = child
            else:
                parent.right = child
        else:
            self.root = child
        del node
#4
    def Q4(self):
        self.postVisit()
        p = self.search_f4()
        self.rotate_left(p)
        print("After rotate: ")
        self.postVisit()
    def search_f4(self):
        lst = []
        lst.append(self.root)
        count = 0
        while len(lst) != 0:
            p = lst.pop()
            if p.right:
            #Sửa điều kiện theo yêu cầu đề bài
                count += 1
            if count == 3:
            # Đề yêu cầu là node thứ mấy thì count bằng bấy nhiêu (ví dụ đề yêu cầu 'first node' thì count = 1
                return p
            if p.left!=None:
                lst.append(p.left)
            if p.right!=None:
                lst.append(p.right)
    def _find_parent(self, root, node):
        if not root:
            return None
        if root.left == node or root.right == node:             
            return root
        if node.val < root.val:
            return self._find_parent(root.left, node)
        else:
            return self._find_parent(root.right, node)
    def rotate_left(self, node):    
        if not node:                                            
            return None
        right_node = node.right                                 
        if not right_node:                                      
            return node
        right_left_node = right_node.left
        node.right = right_left_node                            
        right_node.left = node
        if node == self.root:                                   
            self.root = right_node
        else:                                                   
            parent = self._find_parent(self.root, node)         
            if parent.left == node:                             
                parent.left = right_node
            else:                                               
                parent.right = right_node
        return right_node
    
#5
    def countSecondHighestRating(self):
        highestRating = None
        secondHighestRating = None
        count = 0
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node is not None:
                if highestRating is None or node.info.rating > highestRating:
                    secondHighestRating = highestRating
                    highestRating = node.info.rating
                    count = 1
                elif node.info.rating == highestRating:
                    count += 1
                elif secondHighestRating is None or node.info.rating > secondHighestRating:
                    secondHighestRating = node.info.rating
                    count = 1
                elif node.info.rating == secondHighestRating:
                    count += 1
                stack.append(node.left)
                stack.append(node.right)
        print(f"The numbers of node having second heighest rating: {count}")
        
    def inOrder(self,p):
        if p==None:
            return
        self.inOrder(p.left)
        print(f"{p.info.id, p.info.name, p.info.rating}",end =" - ")
        self.inOrder(p.right)        
    #end def
    def inVisit(self):
        self.inOrder(self.root)
        print("")
    def postOrder(self,p):
        if p==None:
            return
        self.postOrder(p.left)
        self.postOrder(p.right)
        print(f"{p.info.id, p.info.name, p.info.rating}",end =" - ")
    #end def
    def postVisit(self):
        self.postOrder(self.root)
        print("")
        
    def preOrder(self,p):
        if p==None:
            return
        print(f"{p.info.id, p.info.name, p.info.rating}",end =" - ")
        self.preOrder(p.left)
        self.preOrder(p.right)
    #end def
    def preVisit(self):
        self.preOrder(self.root)
        print("")
            
ID = ["A6","A2","A1","A5","A4","A3","B8","A7", "A9","A9","A8"]
Name = ["Mama mia","Panama","Paradise","Tomorrow we fight","Hello","Colors of the wind","Summer in Paris","In a Persian Market", "Love in Paris","Sang pour sang","Memories"]
Rating = [4.0,3.4,4.5,4.5,3.9,4.0,5.0,4.5,3.8,4.8,4.7]
song = BinaryTree()
for i in range(len(ID)):
    song.insert(ID[i], Name[i], Rating[i])
# song.postVisit()
# song.dpblanceFactorMoreThan3()
# song.countSecondHighestRating()
# song.Q3()
# song.Q4()
song.preVisit()