class Solution:
    def twoSum(self, nums, target):
        
        for i, number in enumerate(nums):
            goal = target - number
            start = nums[i + 1]
            stop = len(nums)
            if goal in range(start,stop):
                return [i, nums.index(goal)]

print(Solution.twoSum(Solution, [3,2,3], 6))