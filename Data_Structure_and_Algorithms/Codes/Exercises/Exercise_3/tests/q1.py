test = {
  'name': 'Recap',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> n = 3
          >>> while n >= 1: # In case of infinite loop, type Infinite loop
          ...     n = n - 1
          ...     print(n)
          2
          1
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> n = 0.8
          >>> while n <= 1: # In case of infinite loop, type Infinite loop
          ...     n = n * n
          ...     print(n)
          Infinite loop
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def some_function(i):
          ...     if type(i) == str:
          ...         print('A string')
          ...     else:
          ...         print('Something else')
          >>> some_function('Hello there!' + str(float('3.14')))
          A string
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
