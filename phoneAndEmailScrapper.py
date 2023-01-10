import re
import json

with open('regularExpressionsMockData.json', 'r') as f:
    data = json.load(f)

# create regex for phone numbers
phoneRegex = re.compile(r'''
           (((\d\d\d)|(\(\d\d\d))?  #area code (optional)
           (\s|-)                     #first separator
           \d\d\d                     #three digits
           -                     #second separator
           \d\d\d\d                   #last 4 digits
           (((ext(\.)?\s)|x)         #extension word-part(optional)
           (\d{2,5}))?)                #extension number-part(optional)
           ''', re.VERBOSE)
# create regex for email addresses
emailRegex = re.compile(r'''
                        [a-zA-Z0-9_.+]+    #name part
                        @                   #@ symbol
                        [a-zA-Z0-9_.+]+    #domain name part
                        ''', re.VERBOSE)

# get the text off the clipboard
text = json.dumps(data)
# extract phone/email
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# copy extracted phone/email to clipboard
result = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
print(result)
