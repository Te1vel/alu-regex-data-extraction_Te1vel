
import re
import json
input = "input/raw-text.txt"
with open (input, "r") as file:
    text= file.read()
#this email regex is in the structure of usrename + @ + domain name + domain extansion, (other signs apart from . and -) don't work with domain name
email = r"\b[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
emails = re.findall(email, text)
#using for loop to validate different ALU-specific validation additions
for address in emails:
    if address.endswith("@alueducation.com"):
        print("ALU official:", address)
    elif address.endswith("alumni.alueducation.com"):
        print("ALU alumni:", address)
    elif address.endswith("si.alueducaton.com"):
        print("ALU SI:", address)
    else:
        print("Other emails:", address)
#implementing privacy on emails
local, domain = emails.split("@", 1)
masked_local = []
if len(local) <=2:
    masked_local = local[0] + "*"
else:
    masked_local = local[0] + "*" * (len(local) - 2) + local[-1]
#using regex for credit card number where there's four groups of four digits
credit = r"\b(?:\d{4}[ -]){3}\d{4}\b"
credits = re.findall(credit, text)
#implimenting credit cards privacy
masked_cards = []
for card in credits:
    masked_cards.append("**** **** ****" + card[-4:])
# currency amounts in usd formats
currency = r"\$\s?[0-9]{1,3}(?:,[0-9]{3})*(?:\.[0-9]{2})?\b"
currencies = re.findall(currency, text)
#phone number regex that allows all phone numbers
phone = r"\b(?:\+\d{1,3}[-.\s]?)?\(?\d{1,4}\)?\d{1,4}[-.\s]?\d{1,9}\b"
phones = re.findall(phone, text)

results = {
    "emails": emails,
    "phone": phones,
    "currency": currencies,
    "credit_cards": credits,
    "validation": {
        "status": "completed",
        "external_text_executed": False
    }
}
with open("output/sample-output.json", "w",) as file:
    json.dump(results, file, indent=4)