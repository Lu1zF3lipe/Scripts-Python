words = ('aprender',
         'programar',
         'linguagem',
         'python',
         'curso' )

for c in words:
  print('na palvra "{}" temos: '.format(c.upper()), end=' ')

  for i in c:
    if (i.lower() in 'aeiou'):
      print(i, end=' ')

  print()