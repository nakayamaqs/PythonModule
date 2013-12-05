# from: http://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
# demo: unpacking tuples
def func1(x, y, z):
    print(x,y,z)

def func2(*args):
    print(args)
    args = list(args) # convert tuple to list object
    args[0] = 'Hello'
    args[1] = 'awesome'
    func1(*args)

func2('Goodbye', 'cruel', 'world!')


# demo: unpacking dict
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
