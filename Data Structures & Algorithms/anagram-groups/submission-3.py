from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for str in strs:
            encode_str = [0] * 26
            for letter in str:
                encode_str[ord(letter) - ord("a")] += 1
            hash_key = tuple(encode_str)
            if hash_key not in map.keys():
                map[hash_key] = []
            map[hash_key].append(str)
        return list(map.values())