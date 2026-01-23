class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v,c=0,0
        
        for x in s:
            if x in "aeiou":
                v += 1
            elif "a"<= x and x <= "z":
                c += 1
        if c:return v//c
        return 0