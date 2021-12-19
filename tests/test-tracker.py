"""unit testing for trackers 
"""
import pytest

from modules import tracker as _tracker

def tracker_factory(values):
    tracker = _tracker.GenericTracker()
    tracker.insert(values)
    return tracker


@pytest.mark.parametrize('tracker_class, values, error',
  [
    (_tracker.GenericTracker, "not an array", ValueError),
  ]
)    
def testInsertError(tracker_class, values, error):
    """Error cases for tracker data insertion"""
    tracker = tracker_class()

    with pytest.raises(error):
        tracker.insert(values)

    assert tracker.items == []


@pytest.mark.parametrize('values',
  [
    [1, 2, 3],
  ]
)
def testInsertSuccess(values):
    """Valid cases for tracker data insertion."""
    tracker = _tracker.GenericTracker()
    tracker.insert(values)
    assert tracker.items == values
