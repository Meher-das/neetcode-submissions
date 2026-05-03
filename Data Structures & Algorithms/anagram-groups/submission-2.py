from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for str in strs:
            encode_str = [0] * 26
            for letter in str:
                encode_str[ord(letter) - ord("a")] += 1
            map[tuple(encode_str)].append(str)
        return list(map.values())