# Define a procedure, add_to_index, that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already in the index, add the url to the list of urls associated
# with that keyword.

# If the keyword is not in the index, add an entry to the index: [keyword,[url]]

index = []

#Refactored solution
def add_to_index(index,keyword,url):
    for value in index:
        if value[0] == keyword:
            value[1].append(url)
            return index    
    index.append([keyword, [url]])
    return index


add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
add_to_index(index,'udacity','http://reddit.com')
print index


'''Original solution before I realized how verbose it was

def add_to_index(index,keyword,url):
    if (len(index) > 0):
        i = 0
        j = 1
        while (i < len(index)):
            if (index[i][0] == keyword):
                index[i][j].append(url)
                return index
            i += 1
    index.append([keyword, [url]])
    return index


add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index'''