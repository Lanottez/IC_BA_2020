test = {
  'name': 'For loops',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> temp = 0
          >>> for i in range(5):
          ...     temp += 2
          >>> print(temp)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> cnt1 = 0
          >>> cnt2 = 0
          >>> for i in range(2):
          ...     cnt1 += 1
          ...     for j in range(3):
          ...         cnt2 += 1
          >>> print(cnt1, cnt2)
          2 6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def loop_fun(n):
          ...     x = n
          ...     for i in range(n):
          ...         y = 0         
          ...         for j in range(n):
          ...             y += x
          ...         x += y
          ...     return x
          >>> loop_fun(2)
          18
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
