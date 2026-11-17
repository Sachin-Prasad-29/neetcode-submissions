class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        
        for str in strs:
            counter = [0] * 26
            for ch in str:
                counter[ord(ch) - ord('a')] += 1
                
            hashMap[tuple(counter)].append(str)

        return list(hashMap.values())