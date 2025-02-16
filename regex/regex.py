import re

#Test regex
# Task 1 - Write a regex to extract all phone numbers in the format 123-456-78-90 from the text:
regex = re.compile(r'\d\d\d-\d\d\d-\d\d-\d\d')
text = 'My contacts: 067-901-65-76, 097-123-12-12, and an invalid one 12345.'
numbers = regex.findall(text)
print('Looking for phone numbers here: ' + text)
print('Here is the list:', *numbers)
regex = re.compile(r'((067|097)-\d\d\d-\d\d-\d\d)')  
text = 'My contacts: 067-901-65-76, 097-123-12-12, and an invalid one 12345.'
numbers = regex.findall(text)  # Use findall() to get all matches

print('Looking for phone numbers that start with 067 or 097:', numbers)

# Task 2 Groups - Extract the last 2 digits from a phone number using a regex group.
regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d)-(\d\d)')
text = 'My contacts: 067-901-65-76, 097-123-12-12, and an invalid one 12345.'
numbers = regex.findall(text)
for group in numbers:
    print(f'Here is the list of last 2 digits in number:', group[-1])

# Task 3 Repetitions (*, +, {}): Match the word "Hello" appearing 1 or more times in the sentence:
regex = re.compile(r'(Hello)+')
text = 'HelloHelloHello, how are you?'
textFound = regex.search(text)
print(textFound)

regex = re.compile(r'(Hello){3}')
text = 'HelloHelloHello, how are you?'
textFound = regex.search(text)
print(textFound)

regex = re.compile(r'(\d{3})|12|1234')
text = '123 3432 12313 1234'
textFound = regex.findall(text)
print(textFound)

#Task 4
regex = re.compile(r'(\d\d\d-)?(\d\d\d)-(\d\d)-(\d\d)')
text = 'My contacts: 901-65-76, 097-123-12-12, and an invalid one 12345.'
textFound = regex.findall(text)
print('Looking for phone numbers with or without operator code', textFound)


# regex = re.compile(r'\d\d\d-\d\d\d-\d\d-\d\d')

# text = 'Hello here is my phone number 067-901-65-76, and my friend\'s 097-123-12-12'
# # single match
# number = regex.search(text)
# print("Here is a text to process => " + text)
# print(f'Here is the first number I found {text[number.start():number.end()]}')

# print("Here is a text to process => " + text)
# # multiple match
# phoneNumbers = regex.findall(text)
# print("Here is a list of phone numbers I found in the text: ")
# for i in range(len(phoneNumbers)):
#     print(phoneNumbers[i])

# # group

# regexGroup = re.compile(r'(\d\d)-(\d\d\d-\d\d-\d\d)')
# groups = regexGroup.search(text)
# print("Here is a text to process => " + text)
# print(f'Here is the first operator code I found {groups.group(1)}')

# # ? - 0 or 1
# regexGroup = re.compile(r'(\d\d-)?\d\d\d-\d\d\d-\d\d-\d\d')
# found = regexGroup.search("My phone is 38-065-987-65-47")
# print(found)
# found = regexGroup.search("My phone is 065-987-65-47")
# print(found)

# # * - 0 or more
# # + - 1 or more
# # {3} exect number
# # {3, 5} min repetiton, max rep
# regexGroup = re.compile(r'(Hello)*')
# found = regexGroup.search("Hello")
# print(found)