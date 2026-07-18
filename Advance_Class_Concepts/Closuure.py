def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func

add_five = outer_func(5)
print(add_five(3)) 

#output
#8