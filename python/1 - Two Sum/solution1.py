class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for a, b in enumerate(nums):
      for c, d in enumerate(nums):
        if a != c and b + d == target:
          return [a, c]
    return []