test = {
  'name': 'Functions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def mult(x, y):
          ...     product = x * y
          ...     return product
          >>> mult(5,2)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def some_printing(text):
          ...     if text == 'hey':
          ...         print(text)
          ...     else:
          ...         print('hello')
          >>> some_printing('hi')
          hello
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
          >>> def return_one(): # If there is an error, type Error
          ...     return 1
          >>> return_one()
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> return_one() + 1 # return_one works as in the previous case
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> return_one + 1 # If there's an error, type Error
          Error
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(return_one)
          function
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(return_one())
          int
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def print_one(): # If there is an error, type Error
          ...     print(1)
          ...     return 1
          >>> z = print_one()
          >>> print(z)
          6bbf77c4f4c29b992b7452b251b86eba
          6bbf77c4f4c29b992b7452b251b86eba
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def print_one(): # If there is an error, type Error
          ...     print(1)
          ...     return 1
          >>> print(print_one())
          6bbf77c4f4c29b992b7452b251b86eba
          6bbf77c4f4c29b992b7452b251b86eba
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def print_one(): # If there is an error, type Error
          ...     print(1)
          ...     return None
          >>> z = print_one()
          >>> print(z)
          6bbf77c4f4c29b992b7452b251b86eba
          5a9a47fe60704392d8d7d94a2a818bcc
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def print_one(): # If there is an error, type Error
          ...     print(1)
          >>> z = print_one()
          >>> print(z)
          6bbf77c4f4c29b992b7452b251b86eba
          5a9a47fe60704392d8d7d94a2a818bcc
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> def go(n):
          ...     while n > 0:
          ...         print(n)
          ...         n = n // 2
          >>> go(4)  # If this loops forever, type Infinite Loop.  If it produces an error, write Error. If it displays nothing, write Nothing
          875f61c850489bb83ba79afffd84ec87
          d2b32fc9fa05bf74e7c6bd7e3a7ffdf4
          6bbf77c4f4c29b992b7452b251b86eba
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
