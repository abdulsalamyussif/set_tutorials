import xml.etree.ElementTree as ET

data = '''<person>
<name> Chuck</name>
<phone type = "int1">
0208022754
</phone>
<email hide = "yes"/>
</person>
'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attri: ', tree.find('email').get('hide'))