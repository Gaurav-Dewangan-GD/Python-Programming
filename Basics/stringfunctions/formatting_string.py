# we can format the output data using format method while printing
# or assigning string values

print("Hello you are {0} and I am {1}.".format(45,25))
print("Hello you are {0} and I am {1}.".format(25,45))

# The values inside {} represents the indexex of format numbers
# we can exhange either format parameter or indexes

print("This is {a}. And fun to {b}".format(a="awesome",b="watch"))
print("This is {b}. And fun to {a}".format(a="awesome",b="watch"))

# format can be also used to give spaces and identatation to values
# as well as defining type of data to be formated
print("Value is:{0:4d}".format(24))
print("Value is:{0:6f}".format(9.5645))

# {0:4} represents the spaces for indentation
# {d} and {f} represents type of data i.e decimal and fraction
# {0.2} before represents decimal/floating precision
# if value is specified and we gave another it will show error
