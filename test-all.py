#!/usr/bin/python
"""test-all.py - main testing file
"""

from modules import flatten as _flatten

def _runFlatten(input):
  print 'flatten', input
  flat_res = _flatten.flattenList(input)
  print res

def runFlatten():
  """Flatten lists for demonstration"""

  def _runFlatten(input):
    """Flatten a list, display input and result."""
    print 'flatten', input
    flat_res = _flatten.flattenList(input)
    print '>', flat_res

  _runFlatten([['1', 2, [3]], 4])
  _runFlatten(['1', 2, 3, [4], [], [[[[[[[[[5]]]]]]]]]])


def runTrackers():
  # Examples:

  # >> > temperatures = [22, 7, 22, 13, 2, 31, 18]
  # >> > tracker = TempTracker()
  # >> > tracker.insert(temperatures) # Insert integer data only
  # insertion complete

  # >> > tracker.get_max()
  # 31

  # >> > tracker.get_min()
  # 2

  # >> > tracker.get_mean() # Get the average of all recorded data
  # 16.43
  pass


if __name__ == "__main__":
  runFlatten()
  runTrackers()
