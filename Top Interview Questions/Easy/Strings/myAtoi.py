class Solution:
    def myAtoi(self, s: str) -> int:
        
        t = re.search('^[-+]?[0-9]+',s.strip())
        if(t):
            return(max(-2**31, min(int(t[0]), 2**31-1)))
        else:
            return(0)