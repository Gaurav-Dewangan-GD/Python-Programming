s = "   See you in the space cowboy   \n"

# we can string whitespaces either from left or right
# using rstrip or lstrip with a string

t = s.rstrip()
t = s.lstrip()
print(t)

# since string are immutable their resultant
# should be stored in separate string

l = s.strip()
print(l)

# to find a word/character in string we use find
# index

print(l.find("cow")) # returns start location
print(l.find("tree")) # return -1 not found
# print(l.index("find")) # return's value error not found
# find can also take start and end parameter to search
print(l.find("you",0,len(s)))

# search and replace

test_string = "brown fox grey dog brown fox"
new_string = test_string.replace("brown","black")
print(new_string)

# we can gave a third parameter to change the number of occurence
# of same string
new_string = test_string.replace("brown","black",2)
print(new_string)

# since replace works sequentially it will not 
# get occurence like this
sample = "ababa"
s1 = sample.replace("aba","LL",2)
print(s1) # chanage aba first to LLba their for no aba present
sample_2 = "abaaba"
s2 = sample_2.replace("aba","DD",2)
print(s2)

# splitting string
# suppose we want to create a new_string comparising data from 
# a csv or any other split notation file
# we can fetch and separate data using split
print(new_string.split(" ")) 
# it forms a list to operate upon values
print("this-values-are-dash-separated".split("-"))
print("we[can[also[give[number[of[items[to[take".split("[",3))

# to join them again we can use join method

value_list = "this-values-are-dash-sepearated".split("-")
joiner_string = " "
result = joiner_string.join(value_list)
print(result)

# we can also ommit name for joiner name and can directly join
date = ["23","11","2022"]
print("-".join(date))

# converting case
print(result.capitalize()) # capitalize first letter
print(result.lower())
print(result.upper())
print(result.isupper())
print(result.islower())
print(result.isalpha())
print(result.isnumeric())

# resize the string using center

print("hello".center(30,))
print("hello".center(30,"*"))

# for left and right
print("Bro".ljust(30,"*"))
print("Bro".rjust(30,"*"))