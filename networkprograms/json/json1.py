import json

data = '''
{
    "name":"Yussif",
    "phone":{
        "type":"intl",
        "number":"0208022754"
    },
    "email":{
        "hide":"yes"
    }

}
'''

info = json.loads(data)
print('Name:', info["name"])
print('Email:', info["email"]["hide"])