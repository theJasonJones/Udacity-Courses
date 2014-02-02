''' Define a procedure, lookup, that takes two inputs:
  - an index: list
  - keyword: string

 The procedure should return a list of the urls associated with the keyword. If the keyword
 is not in the index, the procedure should return an empty list. '''

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

def lookup(index,keyword):
    i = 0
    while i < len(index): 
        if (index[i][0] == keyword):
            return index[i][1]
        i += 1
    return index

print lookup(index,'udacity')
print lookup(index, 'computing')
#>>> ['http://udacity.com','http://npr.org']
#>>> ['http://acm.org']