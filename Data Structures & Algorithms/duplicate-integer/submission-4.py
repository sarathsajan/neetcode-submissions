class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_list = []
        for item in nums:
            if item not in check_list:
                check_list.append(item)
            else:
                return True
        return False