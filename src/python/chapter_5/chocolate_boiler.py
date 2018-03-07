# in Python, functions prefixed with double underscore (__) are private
# the __init__ method is private, but it is invoked when you instantiate a class
# all a client needs to do to invoke __init__ is to instantiate your class
# for the singleton pattern, however, you want to control how and when instantiation happens
# what you can do is delegate object creation to a private inner class
# the outer class wraps the inner class and contains a static reference to an instance of the inner class


class ChocolateBoiler:
    instance = None

    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        if not ChocolateBoiler.instance:
            ChocolateBoiler.instance = ChocolateBoiler.__ChocolateBoiler()
        return ChocolateBoiler.instance

    class __ChocolateBoiler:

        def __init__(self):
            self.empty = True
            self.boiled = False

        def fill(self):
            if self.empty:
                self.empty = False
                self.boiled = False

        def drain(self):
            if not self.empty and self.boiled:
                self.empty = True

        def boil(self):
            if not self.empty and not self.boiled:
                self.boiled = True
