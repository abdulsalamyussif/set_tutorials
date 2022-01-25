import json

input = '''
[
    {
        "id": "001",
        "x": "2",
        "name": "Yussif"

    },
    {
        "id":"009",
        "x":"7",
        "name":"salam"

    }
]
'''

info = json.loads(input)
print('User account:', len(info))

for item in info:
    print('Name:', item['name'])
    print('id:', item['id'])
    print('Attribute:', item['x'])