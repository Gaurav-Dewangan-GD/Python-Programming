# In python classes are defined using
# class keyword
import math

class Point:
    def __init__(self,a=0,b=0): #init is always present as constructor functio
        self.x = a  # self is keyword that address that the function/name
        self.y = b  # of class instance it created
    def translate(self,dx,dy): 
        self.x +=dx
        self.y +=dy
    # def showPoint(self):
    #     print("x : {}  y : {}".format(self.x,self.y))
    def distancefromorigin(self):
        self.z = math.sqrt((self.x*self.x)+(self.y*self.y))
        return(self.z)
    def __str__(self):
        return('('+ str(self.x) + ',' + str(self.y)+ ')')
    def __add__(self,val):
        return Point(self.x+ val.x,self.y+val.y)

    
p = Point(2,3)
# p.translate(4,5)
# print(p.distancefromorigin())
p2 = Point(3,4)
p3 = p +p2
print(p3)

# abstraction : same function different implementation

# class Point:
#     def __init__(self,a,b):
#         self.r = math.sqrt((a*a)+(b*b))  # using r^2 = a^2+b^2
#         if a == 0:
#             self.theta = 90
#         else:
#             self.theta = math.atan(b/a)  # x = rcos(theta)
#     def show(self):                      # y = rsin(theta)
#         print(f'x: {round(self.r*math.cos(self.theta))} y : {round(self.r*math.sin(self.theta))}')
# p = Point(3,4)
# p.show()


# class inbuilt function

# __init__ to initialize a constructor

# __str__ to convet object to string 
# similar to str we use for data conversion of values like int and float
# primarily works with print statement

# __add__ to add two objects 
# should be defined correctly based on functionality

# __mult__ to multiply two objects
# __lt__() lower than, ___gt__() greater than
# __le__() less than equal







