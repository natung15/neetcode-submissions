class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict ={}
        for x in s:
            dict[x] = dict.get(x,0) + 1
        for x in t:
            if x not in dict or dict[x] == 0:
                return False
            dict[x] -=1
        return True