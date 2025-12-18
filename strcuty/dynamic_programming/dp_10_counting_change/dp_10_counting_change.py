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

COMPLEXITY:
================================================================================

    a = amount
    c = # coins
    Time: O(a*c)
    Space: O(a*c)


"""

# SOLUTION:
# ================================================================================
def counting_change(amount, coins):
  return _counting_change(amount, coins, 0, {})

def _counting_change(amount, coins, i, memo):
  key = (amount, i)
  if key in memo:
    return memo[key]
  
  if amount == 0:
    return 1
  
  if i == len(coins):
    return 0
  
  coin = coins[i]
  
  total_count = 0
  for qty in range(0, (amount // coin) + 1):
    remainder = amount - (qty * coin)
    total_count += _counting_change(remainder, coins, i + 1, memo)
    
  memo[key] = total_count
  return total_count


      
  

