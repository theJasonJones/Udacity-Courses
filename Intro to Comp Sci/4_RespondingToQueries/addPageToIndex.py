# Define a procedure, add_page_to_index, that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include all of the word occurences found in the
# page content by adding the url to the word's associated url list.

index = []


def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    spaced = content.split()
    for word in spaced:
        add_to_index(index, word, url)
    
    '''i = 0
    while i < len(spaced):
        if spaced[i] not in index:
            index.append(spaced[i])
            index.append([url])
        i +=1
    for i in spaced:
        if i not in index:
            add = []
            add.append(i)
            add.append([url])
            index.append(add)'''
    return index


add_page_to_index(index,'fake.text',"This is a test")
print index
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]


