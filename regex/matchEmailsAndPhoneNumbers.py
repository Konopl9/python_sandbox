import re, pyperclip
# TODO: create a regex to match phone numbers UA format posibilities +38-063-111-11-11, +38-(063)-111-11-11, 063-111-11-11, (063)-111-11-11, +380631111111, 38063111111, 0631111111
phoneNumberRegex = re.compile(
r'''
(
((\+)?38(-)?)?          # (+38-) + - is optional, 38 - is optional to, '-' is optional
((\d{3})|(\(\d{3}\)))   # (063) - () - optional, 3 digits mandatory
-?                      # -
\d{3}                   # 3 digits
-?                      # -
\d{2}                   # 2 digits
-?                      # - 
\d{2}                   # 2 digits
)
''', re.VERBOSE)

# TODO: create a regex to match emails something@something (+_. - can be used)
emailRegex = re.compile(
r'''
[a-zA-Z0-9.+_]+             # first part
@
[a-zA-Z0-9.+_]+
''', re.VERBOSE)

# TODO: get data from a clip board and apply regexs on them
textToParse = pyperclip.paste()
phoneNumbersGroups = phoneNumberRegex.findall(textToParse)
emails = emailRegex.findall(textToParse)

# TODO: extract the data from groups/tuples to list and paste in a formatted way to clipboard
phoneNumbers = []
for phoneGroup in phoneNumbersGroups:
    phoneNumbers.append(phoneGroup[0])
print(phoneNumbers)
print(emails)

result = "\n".join(phoneNumbers) + "\n" + "\n".join(emails)
pyperclip.copy(result)