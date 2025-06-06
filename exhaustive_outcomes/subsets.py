def subsets(elements):
  if not elements: 
    return [[]]
  first = elements[0]
  with_first = []
  without_first = []
  for subset in subsets(elements[1:]):
    with_first.append(
      subset + [first]
    )
    without_first.append(
      subset
    )
  return with_first + without_first