# https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        addends = {}
        for i in range(len(nums)): 
            complement = target - nums[i]
            if complement in addends:
                return [i, addends[complement]]
            else:
                addends[nums[i]] = i