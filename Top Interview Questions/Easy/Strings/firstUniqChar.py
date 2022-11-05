from string import ascii_lowercase

class Solution:
    def firstUniqChar(self, s: str) -> int:
        first = -1
        for char in ascii_lowercase:
            index = s.find(char)
            if index == -1 or s.find(char, index + 1) != -1:
                continue
            if first == -1 or index < first:
                first = index
        return first