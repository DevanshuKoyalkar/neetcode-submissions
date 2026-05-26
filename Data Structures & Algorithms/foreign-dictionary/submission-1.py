class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj_list = defaultdict(list)
        char_set = set()

        for word in words:
            for ch in word:
                char_set.add(ch)


        for i in range(1, len(words)):
            # compare words[i], words[i-1] and get the edge

            word1 = words[i-1]
            word2 = words[i]

            ptr1, ptr2 = 0, 0

            while ptr1 < len(word1) and ptr2 < len(word2) and word1[ptr1] == word2[ptr2]:
                ptr1 += 1
                ptr2 += 1

            # if a prefix no edge skip
            if ptr1 == len(word1):
                continue
            
            if ptr2 == len(word2):
                return ""

            # not a prefix and char where they differ
            ch1 = word1[ptr1]
            ch2 = word2[ptr2]

            adj_list[ch1].append(ch2)
        
        result = []
        visited = set()
        path = set()

        def dfs(node):
            visited.add(node)
            path.add(node)
            for ngbr in adj_list[node]:
                if ngbr in path:
                    return False
                if ngbr in visited:
                    continue
                if not dfs(ngbr):
                    return False
            
            path.remove(node)
            result.append(node)
            return True
        
        for ch in char_set:
            if ch in visited:
                continue
            if not dfs(ch):
                return ""
            

        
        result.reverse()
        return "".join(result)


    
