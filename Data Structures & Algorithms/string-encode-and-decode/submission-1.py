class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for x in strs:
            encoded += str(len(x)) + "#" + x
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = [] 
        i = 0
        j=0
        while i < len(s):
            while s[j] != '#':
                j+=1
            delimiterIndex =  j
            wordLength = int(s[i:delimiterIndex])
            startIndex = delimiterIndex+1
            endIndex = startIndex + wordLength
            decoded.append(s[startIndex:endIndex])
            i= endIndex
            j= endIndex

        return decoded