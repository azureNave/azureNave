class Employee:
    species='Homo Sapiens'
    def __init__(self,name,age):
        self.name=name
        self.age=age
#an instance is an object that’s built from a class and contains real data. An instance of the Dog class is not a blueprint anymore. 
#It’s an actual dog with a name, like Miles, who’s four years old.
#Every time you create a new Dog object, .__init__() sets the initial state of the object by assigning the values of the object’s properties. That is, .__init__() initializes each new instance of the class.
#You can give .__init__() any number of parameters, but the first parameter will always be a variable called self. When you create a new class instance, then Python automatically passes the instance to the self parameter in .__init__() so that Python can define the new attributes on the object.
        
#How Do You Instantiate a Class in Python?
#Creating a new object from a class is called instantiating a class.
    def description(self):
        return f"{self.name} is {self.age} years old"
    def speak(self,language):
        return f"{self.name} says {language}"
#Instance methods are functions that you define inside a class and can only call on an instance of that class. Just like .__init__(), an instance method always takes self as its first parameter.
    
a = Employee("James",32)
a.description()
a.speak("python")