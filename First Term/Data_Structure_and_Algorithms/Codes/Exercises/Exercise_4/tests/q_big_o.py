test = {
  'name': 'Big O ',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'n times',
          'choices': [
            'n times',
            '2n times',
            'n**2 times',
            'log(n) times'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          How many times will Python print 'Hello!'?:
          (n is a positive integer number)
          
          >>> for i in range(n):
          >>>     print('Hello!')
          """
        },
        {
          'answer': 'n**2 times',
          'choices': [
            'n times',
            '2n times',
            'n**2 times',
            'log(n) times'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          How many times will Python print 'Hello!'?:
          (n is a positive integer number)
          
          >>> for i in range(n):
          >>>     for j in range(n):
          >>>         print('Hello!')
          """
        },
        {
          'answer': '2n times',
          'choices': [
            'n times',
            '2n times',
            'n**2 times',
            'log(n) times'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          How many times will Python print 'Hello!'?:
          (n is a positive integer number)
          
          >>> for i in range(n):
          >>>     print('Hello!')
          >>>     print('Hello!')
          """
        },
        {
          'answer': 'log(n) times',
          'choices': [
            'n times',
            '2n times',
            'n**2 times',
            'log(n) times'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          How many times will Python print 'Hello!'?:
          (n is a positive integer number)
          
          >>> while n > 1:
          >>>     n = int(n/2)
          >>>     print('Hello!')
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
