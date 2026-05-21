class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max1=max(candies)
        result=[]
        for i in range(len(candies)):
            x=candies[i]+extraCandies
            if x>=max1:
                result.append(True)
            else:
                result.append(False)
        return result
        
