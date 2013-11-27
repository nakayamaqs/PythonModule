# Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?

def isUniqueChar(input):
    checker = 0
    for c in input:
        # print(c)
        gapValue = ord(c) - ord('a')
        if checker & (1<<gapValue):
            print('find a duplicated character: '+c)
            return False
        checker |=  (1<<gapValue)
    return True


print(isUniqueChar('abcdefg'))
print(isUniqueChar('abcdefga'))
