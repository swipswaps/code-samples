
""" threeSumClosest
Given an array S of n integers, find three integers in S such that the 
sum is closest to a given number, target. Return the sum of the three 
integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums, result, minDif = sorted(nums), None, float("inf")
        for i in range (len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]:
                j, k = i+1, len(nums)-1
                while j < k:
                    diff = nums[i] + nums[j] + nums[k] - target
                    if abs(diff) < minDif:
                        minDif = abs(diff)
                        result = nums[i] + nums[j] + nums[k]
                    if diff < 0: j += 1
                    elif diff > 0: k -= 1
                    else: return target
        return result
            
print(Solution().threeSumClosest([-1, 2, 1, -4], 1)) #2
