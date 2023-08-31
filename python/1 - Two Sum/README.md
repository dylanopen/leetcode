# 1 - Two Sum (Python LeetCode Solution)

This question is asking us to find which two elements in a list add up to the target value.

Difficulty: **Easy**

## Solution 1

``` python
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for a, b in enumerate(nums):
      for c, d in enumerate(nums):
        if a != c and b + d == target:
          return [a, c]
    return []
```

This program simply uses 2 (nested) loops and checks each time whether the numbers add up to `target`.

Once a solution has been found, we return the indexes of those elements.

If there is no solution, we return an empty list.

[View the raw source code](solution1.py)

## Solution 2

``` python
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    keys = {}
    for i, j in enumerate(nums):
      if j in keys:
        return keys[j],i
      else:
        keys[target-j]=i
```

In this program, we:

* Define a dictionary (hashmap) to store the keys
* Loop through the `nums` array (getting the index *and* the value)
* If the `keys` list contains the current number, return the list index of both.
* Otherwise, store the current index in the `keys` dict, with the key being the remaining value needed to reach `target`.

## Links

[Watch the video tutorial][1]

[View the LeetCode problem][2]

[1]: https://youtube.com/watch?v=INSERT_YT_LINK
[2]: https://leetcode.com/problems/two-sum

