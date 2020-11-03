test = {
  'name': 'Lists',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> l1 = [17, 'a', 2, 'tokyo']
          >>> len(l1)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> l1 = [17, 'a', 2, 'tokyo']
          >>> l2 = ['g', 3, 'k']
          >>> len(l1) + len(l2)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> l1 = [17, 'a', 2, 'tokyo']
          >>> l1[2] 
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> l1 = [17, 'a', 2, 'tokyo']
          >>> l1[1:3] # in case of list, write in the following format: [a, b, c, d, e, f]
          ['a', 2]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> l1 = [1, 5, 3]
          >>> for number in l1:
          ...     print(number**2)
          1
          25
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # If there is an error, type Error
          >>> visited_cities = [['Paris', 'France'], ['Berlin', 'Germany'], ['Bucharest', 'Romania']]
          >>> print(visited_cities[0])
          ['Paris', 'France']
          >>> print(visited_cities[2][1])
          Romania
          >>> print(visited_cities[2][2])
          Error
          >>> for pair in visited_cities:
          ...     print(pair[1])
          France
          Germany
          Romania
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # country and its population in millions
          >>> countries = [['France', 65], ['Germany', 80], ['Italy', 60]]
          >>> pop_sum = 0
          >>> for item in countries:
          ...     pop_sum += item[1]
          ...     print(pop_sum)
          65
          145
          205
          >>> for item in countries:
          ...     item[1] += 1
          >>> print(countries[1][1])
          81
          >>> populations = []
          >>> for item in countries:
          ...     populations.append(item[1])
          >>> print(populations)
          [66, 81, 61]
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
