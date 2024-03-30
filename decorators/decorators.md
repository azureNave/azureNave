Decorators allows to modify the behaviour of a function or class.
It allows to wrap another function in order to extend the behaviour of another function, without permanently modifying it.
In other words, it can take inputs, use those inputs to run some pre-defined set of code, and then return an output.

Why use Python decorators?
Python decorators are useful for many reasons, such as:

They allow you to reuse code and avoid repetition. For example, if you have many functions that need to measure their execution time, you can simply apply the same decorator to all of them instead of writing the same code over and over again.

They allow you to separate concerns and follow the principle of single responsibility. For example, if you have a function that performs some complex calculation, you can use a decorator to handle the logging, error handling, caching, or validation of the input and output, without cluttering the main logic of the function.

They allow you to extend the functionality of existing functions or classes without modifying their source code. For example, if you are using a third-party library that provides some useful functions or classes, but you want to add some extra features or behavior to them, you can use decorators to wrap them and customize them to your needs.

Some examples of Python decorators
There are many built-in decorators in Python, such as @staticmethod, @classmethod, @property, @functools.lru_cache, @functools.singledispatch, etc.

https://medium.com/@ayush-thakur02/python-decorators-that-can-reduce-your-code-by-half-b19f673bc7d8

https://www.linkedin.com/pulse/enhancing-spark-functions-python-decorators-divyansh-patel-vrfne#:~:text=This%20decorator%20ensures%20that%20the,that%20might%20otherwise%20go%20unnoticed.

https://medium.com/@machadogj/easier-spark-jobs-logging-with-decorators-b6bd68eab129