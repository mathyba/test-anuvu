"""test-flatten.py - unit testing for flattening utils 
"""

import pytest
from modules import flatten

@pytest.mark.parametrize('input, output',
  [
    ([['1', 2, [3]], 4], ['1', 2, 3, 4]),
    (['1', 2, 3, [4], [], [[[[[[[[[5]]]]]]]]]], ['1', 2, 3, 4, 5]),
    ([[[[], [[]]]], [[['', [[[[[[[0]], False, []]]]]]], None]]], ['', 0, False, None]),
  ]
)
def testFlattenSuccess(input, output):
  res = flatten.flattenList(input)
  assert res == output
  assert isinstance(res, list)
  assert [not isinstance(val, list) for val in res]


@pytest.mark.parametrize('input, error',
  [
    ('not an array', ValueError),
  ]
)
def testFlattenError(input, error):
  with pytest.raises(error):
    flatten.flattenList(input)
