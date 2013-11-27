# Reveal Access python file.
# Source Code from: http://docs.python.org/3.3/howto/descriptor.html#descriptor-example
#

import logging
class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Updating', self.name)
        self.val = val


class RevealAccess_onlyGet(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val


class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5

class MyClass_onlyGet(object):
    x = RevealAccess_onlyGet(100, 'var "x"')
    y = 50

m = MyClass()
print(m.x)
m.x = 20
print(m.x)
print (m.y)
print ("--------")

mc = MyClass_onlyGet()
print(mc.x)
mc.x = 200
print(mc.x)
print (mc.y)

