def npr(items, r):
  if len(items) < r:
    return []
  if r == 0:
    return [[]]
  first = items[0]
  without_first = []
  with_first = []
  for perm in npr(items[1:], r - 1):
    for i in range(len(perm) + 1):
      with_first.append(
        perm[0 : i] + [first] + perm[ i:]
      )
  without_first = npr(items[1:], r)
  return with_first + without_first
  