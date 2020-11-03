test = {
  'name': 'Numpy - Q3',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # fb_returns.  Maybe there's a typo, or maybe you
          >>> # just need to run the cell above this test cell where you defined
          >>> # fb_returns.  (Click that cell and then click the "run
          >>> # cell" button in the menu bar above.)
          >>> 'fb_returns' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(fb_returns)//0.0001 == 3212.0
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
