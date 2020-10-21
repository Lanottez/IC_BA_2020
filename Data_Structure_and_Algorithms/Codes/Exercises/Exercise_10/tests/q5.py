test = {
  'name': 'Pandas_Q5',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # reduced_data.  Maybe there's a typo, or maybe you
          >>> # just need to run the cell above this test cell where you defined
          >>> # reduced_data.  (Click that cell and then click the "run
          >>> # cell" button in the menu bar above.)
          >>> 'reduced_data' in vars()
          6288c15ddc84ed71f21fef2ccf3d56b1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> reduced_data.shape[1] == data.shape[1] - 3
          6288c15ddc84ed71f21fef2ccf3d56b1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> reduced_data.shape[0] == data.shape[0]
          6288c15ddc84ed71f21fef2ccf3d56b1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # It looks like the columns requested to be removed
          >>> # do still exist.
          >>> exists = False
          >>> if 'Cabin' in reduced_data.columns: 
          ...     exists = True
          >>> exists
          1990ab17041489b88701a8b5f74e1e88
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
