def ncr(items, r):
  if r > len(items): return []
  if r == 0: return [[]]
  first = items[0]
  with_first = []
  without_first = []
  for combo in ncr(items[1:], r - 1):
    with_first.append(
      combo + [first]
    )
  without_first = ncr(items[1:], r)
  return with_first + without_first