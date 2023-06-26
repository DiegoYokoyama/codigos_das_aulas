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

