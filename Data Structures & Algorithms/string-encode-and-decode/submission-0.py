class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for x in strs:
            word += str(len(x)) + "#" + x
        return word

    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0
        while i < len(s):
            delimiter = s.index("#",i)
            length = int(s[i:delimiter])
            start = delimiter+1
            end = start + length
            word = s[start:end]
            answer.append(word)
            i = end
        return answer
