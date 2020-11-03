test = {
  'name': 'Numpy - Q5',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # fb_vol.  Maybe there's a typo, or maybe you
          >>> # just need to run the cell above this test cell where you defined
          >>> # fb_vol.  (Click that cell and then click the "run
          >>> # cell" button in the menu bar above.)
          >>> 'fb_vol' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> fb_vol//0.0001 == 161.0
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
