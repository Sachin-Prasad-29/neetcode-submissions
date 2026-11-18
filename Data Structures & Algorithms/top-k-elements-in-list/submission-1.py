class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num,0) + 1
        # print(hashMap)
        tracker = [[] for i in range(len(nums)+1)]
        for key in hashMap.keys():
            tracker[hashMap[key]].append(key)
        res = []
       
        for j in reversed(tracker):
            if len(res) == k:
                    break
          
            for s in j:
                if len(res) == k:
                    break
                res.append(s)
                
                
        return res