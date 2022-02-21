class Solution:
    def reverse(self, x: int) -> int:

        negative = False
        if x < 0:
            negative=True
            x *= -1
        s = str(x) 
        s = "".join([s[len(s)-1-i] for i in range(len(s))])
        
        r = int(s)
        if r > 2**31:
            return 0
        else:
            if negative:
                return -r
            else:
                return r
        