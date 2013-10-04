#comment by zz

def func_5():
    	# print("quitting")
		x = list(range(9))
		print(x)
		print ( list( (x, y) for x in range(1, 3) for y in range(4, 8)) )
		print("Done!")
	# return True
	# print (list(range(6))
# print ( list( (x, y) for x in range(1, 3) for y in range(4, 8)) )
# print (9)

func_5()

def myPrint():
        for item in range(5):
            print("This is the item at " + str(item) + " .")
            print("continue:")            
            print (list(range(item+1)))
            print ( list( (x, y) for x in range(0, item+1) for y in range(4, 8)) )
        return True

myPrint()
