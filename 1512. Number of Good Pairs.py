class Solution:
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] == nums[j]) and (i < j):
                    count += 1
        return count


newNumIdentical = Solution()
print(newNumIdentical.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
