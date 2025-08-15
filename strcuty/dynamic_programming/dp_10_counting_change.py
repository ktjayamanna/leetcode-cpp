# Counting Change - Dynamic Programming Problem
# Count number of ways to make change

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, counting_change, that takes in an amount and a list of coins. The function should return the number of different ways it is possible to make change for the given amount using the coins.

You may reuse a coin as many times as necessary.


EXAMPLES:
================================================================================
For example,

counting_change(4, [1,2,3]) -> 4

There are four different ways to make an amount of 4:

1. 1 + 1 + 1 + 1
2. 1 + 1 + 2
3. 1 + 3
4. 2 + 2

COMMON TRAP:
================================================================================
def counting_change(amount, coins):
    if amount == 0: return 1
    if amount < 0: return 0
    return sum(counting_change(amount - c, coins) for c in coins)

The above solution is wrong because it counts 1+1+2 and 1+2+1 as different ways.


CONSTRAINTS:
================================================================================
[Add constraints here]

"""

# SOLUTION:
# ================================================================================
def counting_change(amount, coins, i = 0, memo = None):
  key = (i, amount)
  if memo is None:
    memo = dict()
  if key in memo:
    return memo[key]
  if amount == 0:
    return 1
  if i == len(coins):
    return 0
  n_ways = 0
  for qty in range(0, amount + 1):
    value = qty * coins[i]
    if value <= amount:
      n_ways += counting_change(amount - value, coins, i + 1, memo)
    else:
      break
  memo[key] = n_ways
  return n_ways
  
      
  

