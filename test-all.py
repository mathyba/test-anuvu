#!/usr/bin/python
"""test-all.py - main testing file
"""

def runFlatten():
  # Examples:

  # >> > flattenList([['1', 2, [3]], 4])
  # ['1', 2, 3, 4]

  # >> > flattenList(['1', 2, 3, [4], [], [[[[[[[[[5]]]]]]]]]])
  # ['1', 2, 3, 4, 5]


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


if __name__ == "__main__":
  runFlatten()
  runTrackers()
