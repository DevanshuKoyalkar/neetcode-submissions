class Solution:
    special_char = ':'

    def encode(self, strs: List[str]) -> str:
        # 10--
        result = ""
        for s in strs:
            size = len(s)
            result += str(size) + self.special_char
            result += s
        return result


    def decode(self, s: str) -> List[str]:
        result = []

        while len(s):
            pos = s.find(self.special_char)
            size = int(s[:pos])

            result.append(s[pos+1:pos+size+1])
            s = s[pos + size + 1:]
        
        return result



