test = {
  'name': 'Strings',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> word = 'hello!'
          >>> print(word[1:3])
          el
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> word = 'hello!'
          >>> len(word)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> word = 'hElLO!'
          >>> print((word.lower()).capitalize())
          Hello!
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> word = 'lovely day'
          >>> count = 0
          >>> for letter in word:
          ...     if letter in 'hey':
          ...         count += 1
          >>> print(count)
          3
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
