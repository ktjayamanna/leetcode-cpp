def counting_change(amount, coins):
  if amount ==  0:
    return 1
  if amount < 0:
    return 0
  sum = 0
  for coin in coins:
    sum += counting_change(amount - coin, coins)
  return sum