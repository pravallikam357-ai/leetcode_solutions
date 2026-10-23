# Problem: Reactangle Area
# Platform: LeetCode
# Difficulty: Medium
# Topic: Math,Geometry
# Language: Python

#  Problem Description:
# Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

#The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

#The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

#  Approach:
# Calculate the width and height of the first rectangle using ax2 - ax1 and ay2 - ay1, then calculate its area.
#Calculate the width and height of the second rectangle using bx2 - bx1 and by2 - by1, then calculate its area.
#Find the overlapping width using min(ax2, bx2) - max(ax1, bx1) and the overlapping height using min(ay2, by2) - max(ay1, by1).
#Use max(0, ...) for both dimensions to ensure the overlap is never negative when the rectangles do not intersect.
#Calculate the overlapping area by multiplying the overlapping width and height.
#Return the sum of both rectangle areas minus the overlapping area, because the overlap must be counted only once.
#  Time Complexity: O(1)
#  Space Complexity: O(1)
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        w1=ax2-ax1
        h1=ay2-ay1
        a1=w1*h1
        w2=bx2-bx1
        h2=by2-by1
        a2=w2*h2
        o1 = max(0, min(ax2, bx2) - max(ax1, bx1))
        o2 = max(0, min(ay2, by2) - max(ay1, by1))
        oh=o1*o2
        return a1+a2-oh
