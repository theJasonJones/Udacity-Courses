def make_hashtable(nbuckets):
  table = []
  for unused_var in range(0, nbuckets):
    table.append([])
  return table

print make_hashtable(5)