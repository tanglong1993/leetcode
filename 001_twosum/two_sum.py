from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        采用双重循环的方式，时间复杂度O(n^2)
        """
        for i, num in enumerate(nums):
            if i < len(nums):
                for j in range(i+1, len(nums)):
                    if num + nums[j] == target:
                        return [i, j]
        return []

    def two_sum2(self, nums: List[int], target: int) -> List[int]:
        """
        采用字典的方式
        """
        value_dict = {}
        for i, num in enumerate(nums):
            if num in value_dict.keys():
                return [value_dict[num], i]
            value_dict[target - num] = i
        return []



if __name__ == "__main__":
    nums = [1, 4, 7, 9, 5, 23, 10]
    target = 12
    solution = Solution()
    print(solution.two_sum(nums, target))
    print(solution.two_sum2(nums, target))
