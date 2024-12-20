def sum_possible(amount, numbers):
  return _sum_possible(amount, numbers, dict())


def _sum_possible(amount, numbers, memo):
  if amount == 0:
    return True
  if amount < 0:
    return False
  if amount in memo:
    return memo[amount]

  for number in numbers:
    if _sum_possible(amount - number, numbers, memo):
      return True
  memo[amount] = False
  return memo[amount]
  
  
