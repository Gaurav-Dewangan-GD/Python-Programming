class Node:
    def __init__(self,initial = None):
        self.val = initial
        self.next = None
    
    def isempty(self):
        if self.val== None:
            return(True)
        else:
            return(False)
    
    def append(self,value):
        if (self.isempty()):
            self.val = value
        elif self.next == None:
            new_node = Node(value)
            self.next = new_node
        else:
            #using loop and a temp pointer
            # temp = self
            # while temp.next != None:
            #     temp = temp.next
            # new_node = Node(value)
            # temp.next = new_node
             # Using recursion
            self.next.append(value)
        return()
    def insert(self,value):
        if(self.isempty()):
            self.val = value
            return()
        else: #insertion from first
            new_node = Node(value) 
            (self.val,new_node.val) = (new_node.val,self.val)
            (self.next,new_node.next) = (new_node,self.next)
        return()
    def deletion(self,value):
        if(self.isempty()):
            return()
        elif self.val == value: # first value is to be deleted
            if self.next == None: # incase of singleton
                self.val = None
            else:
                self.val = self.next.val # second value is copie to first
                self.next = self.next.next # pointer points out to third one
            return()
        else:
            # to move pointer till we find the value to be deleted
            temp  =  self
            while temp.next != None:
                if temp.next.val == value:
                    temp.next = temp.next.next
                else:
                    temp = temp.next
        
        return()

    # to print list
    def __str__(self): # str is a special function for declaring user
                      # defined types print statements genrally in string
        # creating a normal python list to hold value
        selfList = []
        if(self.val == None):
            return(str(selfList))
        else:
            temp = self
            selfList.append(temp.val)
            while temp.next != None:
                temp = temp.next
                selfList.append(temp.val)
        return(str(selfList))

p = Node()
for i in range(1,10):
    p.append(i)
print(p)
p.insert(12)
print(p)
p.deletion(4)
print(p)
        
        
