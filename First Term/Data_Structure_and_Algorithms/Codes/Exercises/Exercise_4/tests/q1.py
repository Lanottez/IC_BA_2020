test = {
  'name': 'q1_recap',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def lsum(L):
          ...     # L is a list with at least two items
          ...     list_sum = L[0]
          ...     for item in L[1:]:
          ...         list_sum =  list_sum + item
          ...     print(list_sum)
          >>> lsum([1, 2, 3])
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> lsum(['a', 'b', 'c'])
          abc
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> x = lsum([2, 2, 1])
          >>> print(x)
          5
          None
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
