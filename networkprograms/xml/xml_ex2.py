import xml.etree.ElementTree as ET

inp = '''
<stuff>
<users>
<user x = "2">
<id>001</id>
<name>Chuck</name>
</user>
<user>
<id>002</id>
<name>Victor</name>
</user>
</users>
</stuff>
'''

stuff = ET.fromstring(inp)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x '))