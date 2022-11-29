# implementing stach using list

list_stack = []
for i in range(0,10):
    list_stack.append(i) # pushed each element
print(list_stack)

# to remove element from back/top use pop
list_stack.pop() 
print(list_stack)
i = 0
while i <=5:
    list_stack.pop()
    i +=1
print(list_stack)

# implementing queue in list

queue_list = []

# to add elements to queue we have add from first
# so append is not an option instead we use inset
for i in range(0,10):
    queue_list.insert(5,i)
print(queue_list)

# delete from front 

i = 0 
while i <=5:
    queue_list.pop()
    i +=1
print(queue_list)
