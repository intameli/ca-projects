persons = [
    {"name": "Jacob","age": 27},
    {"name": "Bob","age": 58},
    {"name": "Jacob","age": 30},
]

arr = ['a','b','c']

test = next((item for item in persons if item['name'] == 'Jacob'), None)
print(test)
test = next((item for item in persons if item['name'] == 'Jacob'), None)

# test = [s+'.' for s in arr]

print(test)
