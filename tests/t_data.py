from datetime import date
dates = [('1:1:2020', r'q=since%3A2020%2D1%2D1'),
         ('-1:4:2020', False),
         ('2:30:2019', False),
         ('', 'q=since%3A{year}%2D{month}%2D{day}'.format(
                year=(t:=date.today()).year,
                month=t.month,
                day=t.day - 1)),
         ]
