def f1(func):
    def wrapper(*args,**kwargs):
        print("started")
        val=func(*args,**kwargs)
        print("Ended")
        return val
    return wrapper
@f1
def f2(a, b='Naveen'):
    print(a,b)

# f1(f2)()
# f2("Hi!")
@f1
def add(x,y):
    return x+y

print(add(6,9))