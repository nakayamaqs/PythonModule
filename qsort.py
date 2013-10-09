# Copyright (c) 2013 the authors listed at the following URL, and/or2 # the authors of referenced articles or incorporated external code:
# http://en.literateprograms.org/Quicksort_(Python)?action=history&offset=20120413011219
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
# Retrieved from: http://en.literateprograms.org/Quicksort_(Python)?oldid=18498

def qsort1(list):
    """
     Quicksort using list comprehensions
     >>> qsort1([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3])
     [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 9]
     >>> qsort1(["bob","alice","barry","zoe","charlotte","fred","marvin"])
     ['alice', 'barry', 'bob', 'charlotte', 'fred', 'marvin', 'zoe']
     """
    if list == []: 
         return []
    else:
         pivot = list[0]
         lesser = qsort1([x for x in list[1:] if x < pivot])
         greater = qsort1([x for x in list[1:] if x >= pivot])
         return lesser + [pivot] + greater
 
from random import randrange
def qsort1a(list):
     """
     Quicksort using list comprehensions and randomized pivot
     >>> qsort1a([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3])
     [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 9]
     >>> qsort1a(["bob","alice","barry","zoe","charlotte","fred","marvin"])
     ['alice', 'barry', 'bob', 'charlotte', 'fred', 'marvin', 'zoe']
     """
     def qsort(list):
         if list == []: 
             return []
         else:
             pivot = list.pop(randrange(len(list)))
             lesser = qsort([l for l in list if l < pivot])
             greater = qsort([l for l in list if l >= pivot])
             return lesser + [pivot] + greater
     return qsort(list[:])
  
def partition(list, l, e, g):
     while list != []:
         head = list.pop(0)
         if head < e[0]:
             l = [head] + l
         elif head > e[0]:
             g = [head] + g
         else:
             e = [head] + e
     return (l, e, g)

def qsort2(list):
     """
     Quicksort using a partitioning function
     >>> qsort2([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3])
     [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 9]
     >>> qsort2(["bob","alice","barry","zoe","charlotte","fred","marvin"])
     ['alice', 'barry', 'bob', 'charlotte', 'fred', 'marvin', 'zoe']
     """
     if list == []: 
         return []
     else:
         pivot = list[0]
         lesser, equal, greater = partition(list[1:], [], [pivot], [])
         return qsort2(lesser) + equal + qsort2(greater)
 
if __name__ == "__main__":
    import doctest     
    doctest.testmod()