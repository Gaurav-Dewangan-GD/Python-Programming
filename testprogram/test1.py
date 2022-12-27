def f():
    global x
    x = 24*57
    y = x
    print(y)
    x = 22
x = 22
print(x)
f()