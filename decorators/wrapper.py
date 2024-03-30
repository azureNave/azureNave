def f1(func):
    def wrapper():
        print("started")
        func()
        print("Ended")
    return wrapper
@f1
def f2():
    print("Hello")

# f1(f2)()
f2()