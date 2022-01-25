def room(x,y,z):
    x = y**2
    z = x / y
    result = x + z
    return result
name = room(2,8,9)
print(name)
print(type(name))