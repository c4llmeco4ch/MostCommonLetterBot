from datetime import date
dates = [('1:1:2020', r'since%3A2020%2D1%2D1'),
         ('-1:4:2020', False),
         ('2:30:2019', False),
         ('%d:%d:%d' % ((t:=date.today()).month, t.day, t.year),
                'since%3A{year}%2D{month}%2D{day}'.format(
                year=t.year,
                month=t.month,
                day=t.day),
         )
       ]

langs = [('en', r'lang%3Aen'),
         ('es', r'lang%3Aes'),
         ('ru', r'lang%3Aru')
        ]
