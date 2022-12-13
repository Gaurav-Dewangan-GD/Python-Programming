# A binary search Tree is a data structure
# generally used to store dynamic values
# that are unique in nature for easier
# updation and deletion at run-time

# similar to priority queue , it has root,
# child nodes and parent nodes with properties
# like
# 1. Value greater than parent node reside right
# 2. Value lesser than parent node to left
# 3. Values are unique in nature

# Note. unlike binary tree it will not request data
# to be placed in order of left to right


class BST:
    def __init__(self,initial = None):
        self.val = initial
        if self.val:
            self.left = BST()  # if value exist generate a node with val and left right none
            self.right = BST()
        else:
            self.left = None   # else all none node
            self.right = None
        return
    
    def isempty(self):
        return(self.val == None)

    def inordertraversal(self):
        if self.isempty():
            return([])
        else:
            return(self.left.inordertraversal() + [self.val] + self.right.inordertraversal())
    
    # to print tree
    def __str__(self):
        return(str(self.inordertraversal()))
    
    # find an element in list
    def find(self,value):
        if self.isempty():
            return(False)
        elif self.val == value:
            return(True)
        elif value > self.val:
            return(self.right.find(value))
        else:
            return(self.left.find(value))

    # finding minimum and maximum in BST
    # left most node is min and right is max

    def minval(self):
        if self.isempty():
            return 
        elif self.left.left == None:
            return(self.val)
        else:
            return(self.left.minval())
    def maxval(self):
        if self.isempty():
            return
        elif self.right.right == None:
            return(self.val)
        else:
            return(self.right.maxval())
    
    # insertion in BST
    # modified using find
    def insert(self,value):
        if self.isempty():
            self.val = value
            self.right = BST()
            self.left = BST()
        elif self.val == value:
            return 
        elif value > self.val:
            return(self.right.insert(value))
        else:
            return(self.left.insert(value))
    

    # to make node empty via
    # putting values none
    def makeempty(self):
        self.val = None
        self.left = None
        self.right = None
        return

    # to check whether the leaf 
    # is empty or not
    def isleaf(self):
       if self.left.left == None and self.right.right == None:
        return True
       else:
        return False  
    
    # function to move right child
    # value to current node

    def copyright(self):
        # copies value to current node
        self.val = self.right.val
        # current node pos will point 
        # left of right node
        self.left = self.right.left
        self.right = self.right.right
        return

    def delete(self,value):
        if self.isempty():
            return 
        if value < self.val:
            self.left.delete(value)
        if value > self.val:
            self.right.delete(value)
        if  value == self.val:
            if self.isleaf():
                self.makeempty()
            # single child
            elif self.left.isempty():
                self.copyright()
            else:
                # for two childs 
                # overwrite the maxvalue to current node
                # and then delete the duplicate one
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
            return
            
# Checking

mytree = BST(23)
# mytree.insert(12)
# mytree.insert(13)
# mytree.insert(56)
# mytree.insert(3)
# mytree.insert(2)
for i in [23,45,78,99,13,12]:
    mytree.insert(i)

print(mytree.find(88))
print(mytree.delete(78))
print(mytree)
