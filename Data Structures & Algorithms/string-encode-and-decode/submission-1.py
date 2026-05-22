class Solution:
    special_char = ':'

    def encode(self, strs: List[str]) -> str:
        # 10--
        encoded_chunks = []
        for s in strs:
            size = len(s)
            encoded_chunks.append(f"{len(s)}{self.special_char}{s}")
        return "".join(encoded_chunks)


    def decode(self, s: str) -> List[str]:
        result = []

        start = 0
        while start < len(s):
            end = s.find(self.special_char, start)
            size = int(s[start:end])

            word_start = end + 1
            word_end = end + 1 + size
            result.append(s[word_start:word_end])

            start = word_end
        
        return result



