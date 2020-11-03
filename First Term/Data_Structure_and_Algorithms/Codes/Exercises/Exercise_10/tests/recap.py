test = {
  'name': 'Recap',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def f(x):
          ...     y = x - 1
          ...     z = y*2
          ...     return y + z
          >>> y = 1
          >>> z = 2
          >>> x = 3
          >>> y = f(z + x)
          >>> print(x, y, z)
          3 12 2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def g(x):
          ...     y = x - 1
          ...     return y
          ...     z = y*2
          ...     return y + z
          >>> x = 1
          >>> y = g(x)
          >>> y
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> x = 1
          >>> while x<=8 or x%2==0:
          ...     x = x+3
          ...     print(x)
          4
          7
          10
          13
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
