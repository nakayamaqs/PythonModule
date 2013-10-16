# A permutation, also called an “arrangement number” or “order,” is a rearrangement of the elements of an ordered list S into a one-to-one correspondence with S itself. A string of length n has n! permutation.
# Source: Mathword(http://mathworld.wolfram.com/Permutation.html)
# Below are the permutations of string ABC.
# ABC, ACB, BAC, BCA, CAB, CBA
# Here is a solution using backtracking.
# From: http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

#Swap values for elements in index i and j of a list
def swap(list, i, j):
    t = list[i]
    list[i] = list[j]
    list[j] = t

####
# Function to print permutations of string
#    This function takes three parameters:
#    1. String
#    2. Starting index of the string
#    3. Ending index of the string.
####
def permunate(list,i,n):
    if(i==n):
        print(*list, sep='') #upack char list into string and print it
    else:
        for j in range(i, n+1):
            # print("i:"+ str(i) + " j: "+ str(j))
            swap(list,i,j)
            permunate(list,i+1,n)
            swap(list,i,j)

l_test = list("abcd")
# swap(l1,0,1)
# print(l1)
# swap(l1,0,1)
# print(l1)

print("----start-----")
permunate(l_test,0,len(l_test)-1)
print("----end-----")
