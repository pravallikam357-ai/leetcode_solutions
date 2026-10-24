# Problem: Count Days Spent Together
# Platform: LeetCode
# Difficulty: Easy
# Topic: Math,Strings
# Language: Python

#  Problem Description:
#Alice and Bob are traveling to Rome for separate business meetings.You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.
#Return the total number of days that Alice and Bob are in Rome together.
#You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

#  Approach:
# Create a list containing the number of days in each month.
#Convert each date from "MM-DD" format into a day number of the year using a helper function.
#Find the later arrival date using max() to get the common starting day.
#Find the earlier leaving date using min() to get the common ending day.
#If the starting day is greater than the ending day, return 0.
#Otherwise, return end - start + 1 to count all overlapping days, including both endpoints.
#  Time Complexity: O(1)
#  Space Complexity: O(1)
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30,
                         31, 31, 30, 31, 30, 31]

        def convert(date):
            month, day = map(int, date.split('-'))

            total = day

            for i in range(month - 1):
                total += days_in_month[i]

            return total

        start = max(convert(arriveAlice), convert(arriveBob))
        end = min(convert(leaveAlice), convert(leaveBob))

        if start > end:
            return 0

        return end - start + 1   
