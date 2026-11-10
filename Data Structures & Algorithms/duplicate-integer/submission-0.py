class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False
        count_kv = {}
        
        for item in nums:
            if not count_kv.get(item):
                count_kv[item] = 1
            else:
                flag = True
                return flag
        return flag