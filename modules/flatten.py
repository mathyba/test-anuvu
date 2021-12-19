#!/usr/bin/python
"""flatten.py - extended utils
"""

def flattenList(nestedList):
  """Flatten nested arrays.

  Args:
    nestedList (list): array with possibly nested arrays

  Raises:
    ValueError: if attempting to flatten something that isn't a list

  Returns:
    A list of all non-empty values nested within the given array.
    Ignores only [], preserves all other falsish values
  """

  if not isinstance(nestedList, list):
    raise ValueError("Trying to flatten", nestedList, '- expected a list.')

  flatList = []
  for val in nestedList:
    flatList.extend(flattenList(val) if isinstance(val, list) else [val])

  return flatList
