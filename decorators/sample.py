def inner_function():
	print("inner_function is called")
    
def outer_function(func):
    print("outer_function is called")
    func()
#Here inner_function is referenced as an object calls the function. So it can passed as an
#arugment, stored in a variable. So calling outer_function, pass through the object func
#that references inner_function, then calling func inside outer_function.
outer_function(inner_function)