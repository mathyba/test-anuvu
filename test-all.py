#!/usr/bin/python
"""test-all.py - main testing file
"""

from modules import (
  flatten as _flatten,
  tracker as _tracker,
)

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
  """Run trackers for demonstration"""

  def _runTracker(data, tracker_class=_tracker.GenericTracker):
    """Run tracker and output details"""
    tracker = tracker_class()
    print "running instance of", tracker.__class__.__name__
    tracker.insert(data)
    print "insertion complete"

  _runTracker(_tracker.GenericTracker, [22, 7, 22, 13, 2, 31, 18])


if __name__ == "__main__":
  runFlatten()
  runTrackers()
