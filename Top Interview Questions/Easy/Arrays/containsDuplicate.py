from re import L


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        '''
        if len(nums) == len(set(nums)):
            return False
        
        return True
        This solution is very slow
        '''

        s = set()

        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        
        return False