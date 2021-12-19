"""unit testing for trackers 
"""
import pytest

from modules import tracker as _tracker

def tracker_factory(tracker_class, values=[1, 2, 3, 4, 5, 42]):
    """Tracker factory for test use.

    Args:
        tracker_class: tracker class to instantiate
        values: list of integers to insert in tracker

    Returns:
        A tracker instance of given <tracker_class> with <values> inserted.
    """
    tracker = tracker_class()
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

@pytest.mark.parametrize('values, expected_mean',
  [
    ([1, 2], 1.5),
    ([], None),
    ([-1, 0, 1], 0),  ]
)
def testMean(values, expected_mean):
    tracker = tracker_factory(_tracker.GenericTracker, values)
    mean = tracker.mean
    assert mean == expected_mean
    assert mean is None or isinstance(mean, float)
    if mean is not None:
        assert 100 * mean == int(mean * 100)
