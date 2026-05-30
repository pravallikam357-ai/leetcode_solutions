class Solution(object):
    def uniqueOccurrences(self, arr):
        counts=[]
        for i in set(arr):
            count=arr.count(i)
            counts.append(count)
            if len(counts)!=len(set(counts)):
                return False
        return True
