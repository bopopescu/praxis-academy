class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hallo sayang akoh', self.name)

p = Person('pradana yoga')
p.say_hi()