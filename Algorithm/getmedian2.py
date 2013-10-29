# Question described in getmedian.py
# The algorithms is slighly different, running time is still O(lgn)

# Method 3 (By doing binary search for the median):
# The basic idea is that if you are given two arrays ar1[] and ar2[] and know the length of each, you can check whether an element ar1[i] is the median in constant time. Suppose that the median is ar1[i]. Since the array is sorted, it is greater than exactly i values in array ar1[]. Then if it is the median, it is also greater than exactly j = n – i – 1 elements in ar2[].
# It requires constant time to check if ar2[j] <= ar1[i] <= ar2[j + 1]. If ar1[i] is not the median, then depending on whether ar1[i] is greater or less than ar2[j] and ar2[j + 1], you know that ar1[i] is either greater than or less than the median. Thus you can binary search for median in O(lg n) worst-case time.

# For two arrays ar1 and ar2, first do binary search in ar1[]. If you reach at the end (left or right) of the first array and don't find median, start searching in the second array ar2[].

# 1) Get the middle element of ar1[] using array indexes left and right.
#    Let index of the middle element be i.
# 2) Calculate the corresponding index j of ar2[]
#      j = n – i – 1
# 3) If ar1[i] >= ar2[j] and ar1[i] <= ar2[j+1] then ar1[i] and ar2[j]
#    are the middle elements.
#      return average of ar2[j] and ar1[i]
# 4) If ar1[i] is greater than both ar2[j] and ar2[j+1] then
#      do binary search in left half  (i.e., arr[left ... i-1])
# 5) If ar1[i] is smaller than both ar2[j] and ar2[j+1] then
#      do binary search in right half (i.e., arr[i+1....right])
# 6) If you reach at any corner of ar1[] then do binary search in ar2[]

# below are the improved python sourcecode by myself
def getMedian(list1, list2, left, right, n):

    # We have reached at the end (left or right) of list1[]
    if left > right:
        print("Swith list1 & list2")
        return getMedian(list2, list1, 0, n-1, n)

    i = (left + right) // 2
    j = n - i - 1

    print("Info: List1[{i}]={0}, list2[{j}]={1}, (left,right) = ({left},{right}) ".format(list1[i],list2[j], j=j, i=i, left=left, right=right))

    # when list1[i] is in between list2[j] and list2[j+1], or greater than list2[n-1]
    if list1[i] > list2[j] and (j == n-1 or list1[i] <= list2[j+1]):
         # ar1[i] is decided as median 2, now select the median 1 (element just before ar1[i] in merged array) to get the average of both
        if (i == 0 or list2[j] > list1[i-1]):
            return (list1[i] + list2[j])/2;
        else:
            return (list1[i] + list2[i-1])/2;
    # when list1[i] is greater than list2[j] and list2[j+1]
    elif list1[i] > list2[j] and j != n-1 and list1[i] > list2[j+1]:
        # print('i:'+ str(i) + "*    j:" + str(j))
        return getMedian(list1, list2, left, i-1, n)

    else:
        # print('i:'+ str(i) + "&    j:" + str(j))
        return getMedian(list1, list2, i+1, right, n)

def runGetMedian(list1, list2,  n):
    #// If all elements of list1 are greater then median is average of first element of list1 and last element of list2
    if list1[0] >= list2[n-1]:
        return (list1[0] + list2[n-1]) / 2
    elif list2[0] >= list1[n-1]:
        return (list2[0] + list1[n-1]) / 2
    else:
        return getMedian(list1, list2, 0, n-1, n)

list1 = [1, 12, 15, 26, 38]
list2 = [2, 13, 17, 30, 45]
print(runGetMedian(list1,list2,len(list1)))

list1 = [1, 2, 3, 7, 19, 24, 57]
list2 = [4, 7, 9, 10, 12, 13, 69]
print(runGetMedian(list1,list2, len(list1)))

list1 = [1, 2]
list2 = [4, 7]
print(runGetMedian(list1,list2,len(list1)))
