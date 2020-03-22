from datetime import date
dates = [('1:1:2020', 'https://api.twitter.com/1.1/search/tweets.json?' +
                      'q=since%3A2020%2D1%2D1'),
         ('-1:4:2020', False),
         ('2:30:2019', False),
         ('', 'https://api.twitter.com/1.1/search/tweets.json?' +
              'q=since%3A%d%2D%d%2D%d' % (
                (t:=date.today()).year, t.month, t.day - 1)),
         ]
