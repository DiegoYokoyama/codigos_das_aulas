import pprint
data = {'name': 'John', 'age': 30, 'city': 'New York'}

pprint.pprint(data)
#--------------------------------------------------------------
data = {'name': 'John', 'age': 30, 'city': 'New York'}

formatted_data = pprint.pformat(data)
print(formatted_data)
#--------------------------------------------------------------
data = {'name': 'John', 'age': 30, 'city': 'New York'}

readable = pprint.isreadable(pprint.pformat(data))
print(readable)
#--------------------------------------------------------------
data = {'name': 'John', 'age': 30, 'city': 'New York'}
data['self'] = data

recursive = pprint.isrecursive(data)
print(recursive)
#--------------------------------------------------------------

#https://docs.python.org/3/library/pprint.html
#https://chat.openai.com/c/ee456ace-9b38-44dd-a914-ec4f2a556d96