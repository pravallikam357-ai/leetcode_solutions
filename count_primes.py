# Problem: Count primes
# Platform: LeetCode
# Difficulty: Medium
# Topic: Arrays
# Language: Python

#  Problem Description:
# Given an integer n, return the number of prime numbers that are strictly less than n.

#  Approach:
# If n <= 2, return 0 because there are no prime numbers less than 2.
#Create a boolean array prime of size n and initialize all values to True.
#Mark 0 and 1 as False since they are not prime.
#Start with p = 2.
#While p * p < n:
#If prime[p] is True, then p is a prime number.
#Mark all multiples of p starting from p * p as False.
#Increase p by 1 and repeat.
#Finally, count all the True values in the array using:

#  Time Complexity: O(n log log n)
#  Space Complexity: O(n)
class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0

        prime = [True] * n
        prime[0] = prime[1] = False

        p = 2
        while p * p < n:
            if prime[p]:
                for i in range(p * p, n, p):
                    prime[i] = False
            p += 1

        return sum(prime)
