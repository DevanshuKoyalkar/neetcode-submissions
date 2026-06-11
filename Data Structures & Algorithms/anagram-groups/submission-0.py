class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            anagram_map[tuple(sorted(s))].append(s)

        return list(anagram_map.values())