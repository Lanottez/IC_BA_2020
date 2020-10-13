test = {
  'name': 'Numpy - Q4',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # highest_FB_daily_returns.  Maybe there's a typo, or maybe you
          >>> # just need to run the cell above this test cell where you defined
          >>> # highest_FB_daily_returns.  (Click that cell and then click the "run
          >>> # cell" button in the menu bar above.)
          >>> 'highest_FB_daily_returns' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> highest_FB_daily_returns//0.0001 == 504.0
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
