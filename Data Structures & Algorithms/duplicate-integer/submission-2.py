class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_kv = {}
        for item in nums:
            if item not in count_kv:
                count_kv[item] = 1
            else:
                return True
        return False