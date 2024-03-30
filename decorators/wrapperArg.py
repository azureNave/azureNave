def f1(func):
    def wrapper(*args,**kwargs):
        print("started")
        func(*args,**kwargs)
        print("Ended")
    return wrapper
@f1
def f2(a, b='Naveen'):
    print(a,b)

# f1(f2)()
f2("Hi!")