class Solution:
    def reverse(self, x: int) -> int:

        # reverse the number
        if x < 0:
            x = -1 * int(str(x)[1:][::-1])

        else:
            x = int(str(x)[::-1])

        # check if the number is within the range
        if x < -2**31 or x > 2**31 - 1:
            return 0

        return x
        