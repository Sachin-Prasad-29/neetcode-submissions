class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,v in enumerate(nums):
            if target - v in map and i != map[target - v]:
                return [map[target - v],i]
            map[v] = i

            
            