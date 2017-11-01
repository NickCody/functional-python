import itertools
flatten = itertools.chain.from_iterable

scoring = (7, 3, 2, 6, 1)

def dist(list_of_tup, i):
  return tuple(map(lambda one_tup: one_tup + (i,), list_of_tup))

def t2a(t):
  return map(lambda v: v, t)

def valid(t):
  if len(t) == 0:
    return True
  elif t[0] == 1:
    return False
  elif t[0:3] == (6,1):
    return valid(t[2:])
  else:
    return valid(t[1:])

def combine(total_score):
  if total_score <= 1:
    return ((),)

  possibles = tuple(flatten(map(lambda p: dist(combine(total_score - p), p), scoring)))
  solutions = filter(lambda scores: sum(t2a(scores)) == total_score and valid(scores), possibles)

  return solutions

def unique(solutions):

  sorted_solutions = map(lambda series: tuple(sorted(series)), solutions)
  unique_solutions = set(sorted_solutions)
  return unique_solutions

score = input ("Enter an integer greater than 1 : ")

print("All Solutions:")
for series in combine(score):
  print series

print("Unique Solutions:")
for series in unique(combine(score)):
  print series


