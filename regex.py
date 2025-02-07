import re

regex = re.compile(r'\d\d\d-\d\d\d-\d\d-\d\d')

text = 'Hello here is my phone number from UA 067-901-65-76, and my mom\'s 097-123-12-12'
number = regex.search(text)
print(f'Here is the first number I found {text[number.start():number.end()]}')

phoneNumbers = regex.findall('Hello here is my phone number from UA 067-901-65-76, and my mom\'s 097-123-12-12')
for i in range(len(phoneNumbers)):
    print(phoneNumbers[i])