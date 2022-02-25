def outer_func():
    # --------------------------------------------------------------------
    # this part is called a closure
    x = 'python'

    def inner_func():
        print('{0} rocks!'.format(x))  # x is called a free variable
    # --------------------------------------------------------------------
    inner_func()  # The value of x is looked up when inner gets called


# calling outer will lead to the print out of "python rocks"
outer_func()
print('-----------------------------------------------------')

# instead calling inner_func inside outer_func we can return it


def outer_func():
    x = 'python'

    def inner_func():
        print('{0} rocks!'.format(x))  # x is called a free variable
    return inner_func

# by the time we call inner_func outer_func has stopped running, and therefore
# it seems logical that the x-variable should no longer be available since
# the outer_func-scope is gone. But this is not the case. Python creates an
# intermediary object that points to "python", which both x-variables in
# outer_func and inner_func points to. So now x is still available inside
# inner_func


# so now we can store outer_func as a variable and then call the variable
fn = outer_func()
fn()

print('-----------------------------------------------------')

# we can also do this - this will do the same thing
outer_func()()

print('-----------------------------------------------------')

print(fn.__code__.co_freevars)  # this will print out the free variables
# this will print out cell address of the intermediary cell and the adddress it points to
print(fn.__closure__)

print('-----------------------------------------------------')
