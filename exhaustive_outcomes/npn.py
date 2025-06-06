def npn(items):
  if not items: 
    return [[]]
  first = items[0]
  out = []
  for perm in npn(items[1:]):
    for i in range(len(perm) + 1):
      out.append(
        perm[0 : i] + [first] + perm[i:]
      )
  return out