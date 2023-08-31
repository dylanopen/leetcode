class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    keys = {}
    for i, j in enumerate(nums):
      if j in keys:
        return keys[j],i
      else:
        keys[target-j]=i