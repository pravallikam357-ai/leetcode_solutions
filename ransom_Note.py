class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        for ch in ransomNote:
            if magazine.count(ch) < ransomNote.count(ch):
                return False

        return True
