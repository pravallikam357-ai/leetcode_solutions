# Problem: Boats to save people
# Platform: LeetCode
# Difficulty: Medium
# Topic: Arrays,Two pointers,Greedy,Sorting
# Language: Python

#  Problem Description:
# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

#Return the minimum number of boats to carry every given person..

#  Approach:
#Sort the people array.
#Use two pointers:
#i → lightest person
#j → heaviest person
#If the lightest and heaviest person can share a boat (people[i] + people[j] <= limit):
#Put them together and move i forward.
#The heaviest person (j) always gets on a boat, so move j backward.
#Count one boat for each iteration.
#Continue until all people are assigned boats..

#  Time Complexity: O(n log n)
#  Space Complexity: O(n)
class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        
        i = 0
        j = len(people) - 1
        boats = 0
        
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1   
            j -= 1       
            boats += 1
        
        return boats
