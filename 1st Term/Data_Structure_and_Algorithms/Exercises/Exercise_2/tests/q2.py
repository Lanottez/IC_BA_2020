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
          1
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def print_one(): # If there is an error, type Error
          ...     print(1)
          ...     return 1
          >>> print(print_one())
          1
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def print_one(): # If there is an error, type Error
          ...     print(1)
          ...     return None
          >>> z = print_one()
          >>> print(z)
          1
          None
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def print_one(): # If there is an error, type Error
          ...     print(1)
          >>> z = print_one()
          >>> print(z)
          1
          None
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
          >>> def go(n):
          ...     while n > 0:
          ...         print(n)
          ...         n = n // 2
          >>> go(4)  # If this loops forever, type Infinite Loop.  If it produces an error, write Error. If it displays nothing, write Nothing
          4
          2
          1
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
