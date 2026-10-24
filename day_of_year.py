# Problem: Day of the Year
# Platform: LeetCode
# Difficulty: Easy
# Topic: Math,Strings
# Language: Python

#  Problem Description:
# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

#  Approach:
# Extract the date: Split the given date string using - and use map(int, ...) to convert the year, month, and day into integers.
#Initialize month days: Store the number of days in each month in a list, assuming February has 28 days.
#Check the leap year: If the year is divisible by 400, or divisible by 4 but not by 100, update February to 29 days.
#Calculate previous days: Iterate through the months before the given month and add their days to a.
#Calculate the result: Add the given day d to a and return the total.

#  Time Complexity: O(1)
#  Space Complexity: O(1)
class Solution:
    def dayOfYear(self, date: str) -> int:
        y,m,d=map(int,date.split("-"))
        a=0
        m_d=[31,28,31,30,31,30,31,31,30,31,30,31]
        if y%400==0 or (y%4==0 and y%100!=0):
            m_d[1]=29
        else:
            m_d[1]=28
        for i in range(m-1):
            a=a+m_d[i]
        f=a+d  
        return f
