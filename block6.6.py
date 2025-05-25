class Lister:
    def __str__(self):
        indirect = self.__class__.__bases__  # Get super classes
        return f"<Instance of {self.__class__.__name__}({', '.join([c.__name__ for c in indirect])}), address {id(self)}:\n" + \
               '\n'.join(attr + '=>' + str(getattr(self, attr))
                         for attr in self.__dict__) + '>'

if __name__ == '__main__':
    class Super:
        def __init__(self):
            self.age = 40

    class Sub(Super, Lister):
        def __init__(self):
            Super.__init__(self)
            self.name = 'Bob'

    x = Sub()
    print(x)
