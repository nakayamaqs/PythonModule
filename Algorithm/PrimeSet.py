
# From: http://www.geeksforgeeks.org/forums/topic/google-interview-question-for-software-engineerdeveloper-fresher-about-algorithms-20/
# Question:
# Given a set of numbers [1-N] . Find the number of subsets such that the sum of numbers in the subset is a prime number.
#

import math
import logging
import pprint

def isPrime(number):
    squarroot = math.floor(math.sqrt(number))
    for i in range(2,squarroot+1):
        if number % i == 0:
            return False
    return True

def CheckPrime_ForSet(index, num, prime_set_result):
    logging.info("Begin, index=" + str(index) + " num=" + str(num))
    # print(prime_set_result)

    global prime_count

    # check if (num + current_SetSum) is prime
    for i in range(index,-1,-1):
        if len(prime_set_result[i]) > 0:
            # print('reveal sub list: '+ str(prime_set_result[i]))
            for j in range(len(prime_set_result[i])-1, -1, -1):
                prime_set_result[i+1].append(prime_set_result[i][j] + num)
                if isPrime(prime_set_result[i][j] + num):
                    prime_count+=1

    # check if current number is prime, append to list[0] nomatter if it is Yes.
    prime_set_result[0].append(num)
    if isPrime(num):
        prime_count+=1
    logging.info("Finish, prime_count = " + str(prime_count) + str(prime_set_result))

global prime_count
def CheckSet(num_list):
    num_list = list(set(num_list)) #get disctinct elements from input list
    num_list.sort()
    prime_set_result = [ [] for x in range(len(num_list))]
    global prime_count
    prime_count = 0

    for i, n in enumerate(num_list):
        CheckPrime_ForSet(i, n, prime_set_result)

    return prime_count,prime_set_result


def dy_CheckPrimeSet(num_list):
    num_list = list(set(num_list)) #get disctinct elements from input list
    num_list.sort()
    prime_set_result = [ [] for x in range(len(num_list))]
    global prime_count
    prime_count = 0

    # init prime_set_result[0]
    for i in num_list:
        prime_set_result[0][i] = num_list[i]
        if isPrime(num):
            prime_count+=1

    for l in range(len(num_list)):
        for j in range(l,len(num_list)):
            for i in range(j, len(num_list) - j + 1):
                print("l="+str(l) + "  j="+str(j) + "  i="+str(i))



# print(isPrime(10))
# print(isPrime(13))
# print(isPrime(19))
# print(isPrime(323))

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)
num_list, set_result = CheckSet([3,7,12,4,7,23,24,59])
# 24,59
logging.info("Num of prim subsets =" + str(num_list) + ", Prim set result =" + str(set_result))
# pp = pprint.PrettyPrinter(depth=2)
for i in range(len(set_result)):
    print(str(i)+": "+ str(set_result[i]))

# pprint.pprint(set_result)
# dy_CheckPrimeSet([3,7,12,4,7,23,])
