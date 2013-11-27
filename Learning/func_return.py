# from :http://docs.python.org/3.3/faq/programming.html#what-is-the-difference-between-arguments-and-parameters

# By returning a tuple of the results:
def func2(a, b):
    a = 'new-value'        # a and b are local names
    b = b + 1              # assigned to new objects
    return a, b            # return new values

x, y = 'old-value', 99
x, y = func2(x, y)
print(x, y)                # output: new-value 100


# By passing a mutable (changeable in-place) object:
def func1(a):
    a[0] = 'new-value'     # 'a' references a mutable list
    a[1] = a[1] + 1        # changes a shared object

args = ['old-value', 99]
func1(args)
print(args[0], args[1])    # output: new-value 100


# By passing in a dictionary that gets mutated:
def func3(args):
    args['a'] = 'new-value'     # args is a mutable dictionary
    args['b'] = args['b'] + 1   # change it in-place

args = {'a':' old-value', 'b': 99}
func3(args)
print(args['a'], args['b'])


# Or bundle up values in a class instance:
class callByRef:
    def __init__(self, **args):
        for (key, value) in args.items():
            setattr(self, key, value)

def func4(args):
    args.a = 'new-value by func4.'        # args is a mutable callByRef
    args.b = args.b + 100         # change object in-place

args = callByRef(a='old-value', b=99,c=23)
func4(args)
print(args.a, args.b, args.c)
