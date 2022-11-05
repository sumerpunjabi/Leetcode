from string import ascii_lowercase

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for x in ascii_lowercase:
            if s.count(x) != t.count(x):
                return False
        return True