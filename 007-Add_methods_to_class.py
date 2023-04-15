def add_to_class(Class):  #@save
    """Register functions as methods in created class."""
    def wrapper(obj):
        setattr(Class, obj.__name__, obj)
    return wrapper


class A:
    def __init__(self):
        self.b=1
        self.a=2

a = A()

@add_to_class(A)
def new_method(self):
    print('this is a method added to class A from outside, it says', self.b)

@add_to_class(A)
def new_method2(self):
    print('this is another method added to class A from outside, it says', self.a)

a.new_method()
a.new_method2()