class MyPrint:
 
  def __init__(self):
    pass
 
    def myPrint(self):
        for item in range(10):
            print("This is the item at " + str(item) + " .")
        return True
 
class MyPrint_Test():
 
    p = None
 
    @classmethod
    def setup_class(cls):
        cls.p = MyPrint()
 
    @classmethod
    def teardown_class(cls):
        cls.p = None
 
    def myPrint_test(self):
        assert p.myPrint()