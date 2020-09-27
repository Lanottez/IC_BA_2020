test = {
  'name': 'Recap',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print(4 * 3) # If there is an error, type Error
          12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> x = 2
          >>> y = 3
          >>> x = (y + 1)*x 
          >>> print(x) # If there is an error, type Error
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> temp = 30
          >>> print('Temp: ' + temp) # If there is an error, type Error
          Error
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> x = 8
          >>> x < 5
          False
          >>> x > 0 and x < 7
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> name = 'Franz'
          >>> if name == 'Franz':
          ...     print('Hello ' + name)
          Hello Franz
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> y = 7
          >>> while y > 0: # In case of infinite loop, type Infinite loop
          ...     y = y // 2
          ...     print(y)
          3
          1
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> y = 2
          >>> while y != 0: # In case of infinite loop, type Infinite loop
          ...     y = y // 2
          ...     print(y)
          1
          0
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
