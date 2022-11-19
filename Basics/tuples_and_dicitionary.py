# tuples can be used in 
# mulitple ways

# simulatneous assignment
(a,b,c) = (True,"Hello",[2,3,4])

# a tuple, quadraple, or triplet values
# can be assinged

point = (3.5,4.8)
date =(18,11,2022)

# Access 

print(point[0])
print(date[0:])

# for i in date:
#     print(i,end="-")
# tuples are immutanle in nature
# point[1] = 25


# Dicitionary
# It is termed as an associative array
# where instead of using 0 to n numbers
# as index we use immutable types like
# int,float,string,tuple to address indexes
# as keys

# Declaration

hello_world = {
    "Descripiton":'''A common term 
                    used to express print 
                    statement in programming''',
    "domain":"Computer science",
    "type": "string"
}

#quick assingment
football_score = {}
football_score["Ronaldo"] = 23
football_score["Messi"] = 45
football_score["Hulk"] = 12
print(hello_world)
print(football_score)


# nested Dicitionary

test_match = {
    "Inning_1":{
        "Kohli":43,
        "dhawan":20,
        "Rohit":0
    },    
    "Inning_2":{
        "Kohli":23,
        "dhawan":0,
        "Rohit":100
    },    
    "Inning_3":{
        "Kohli":13,
        "dhawan":120,
        "Rohit":10
    }
}

print(test_match["Inning_2"]["Kohli"])

# dicitionary values are mutubale in nature

# print(test_match["Inning_3"]["Rohit"])
# test_match["Inning_3"]["Rohit"] = 245
# print(test_match["Inning_3"]["Rohit"])


# looping over keys
# we can extract keys using the
# the key methods as dicitionary.keys()
for k in test_match.keys():
    print(test_match[k])

# dicitionary values can not be present
# in sorted form by default 
# therefore we use sort method

for k in sorted(football_score.keys()):
    print(k)
# sorted generated a sequence of values
# not list

# sample mapping
# d = {}
# for i in  "abcd":
#     d[i] = 0

# for j in "abhijeet":
#     for i in d.keys():
#         if j in i:
#             d[i] +=1
# print(d)

# list can add keys as well as value on allocation 
# as we have seen first
print(football_score)
football_score["Neymar"] = 90
print(football_score)
for j in football_score.values():
    print(j)
