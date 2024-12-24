def non_adjacent_sum(nums):
  return _non_adjacent_sum(nums, 0, dict())

def _non_adjacent_sum(nums, i, memo):
  if not nums: return 0
  if i in memo: return memo[i]
  if i >= len(nums): return 0
  include = nums[i] + _non_adjacent_sum(nums, i + 2, memo)
  exclude = _non_adjacent_sum(nums, i + 1, memo)
  memo[i] = max(include, exclude)
  return memo[i]
  
  
