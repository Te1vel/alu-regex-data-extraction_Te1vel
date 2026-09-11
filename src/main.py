
import re
import json
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT = BASE_DIR/ "input" / "raw-text.txt"
OUTPUT = BASE_DIR / "output" / "sample-output.json"
with open (INPUT, "r") as file:
    text= file.read()
#this email regex is in the structure of usrename + @ + domain name + domain extansion, (other signs apart from . and -) don't work with domain name
email = r"\b[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
emails = re.findall(email, text)
#using for loop to validate different ALU-specific validation additions
masked_emails = []
alu_counts = {
    "Official": 0,
    "Alumni": 0,
    "SI": 0,
    "Other": 0,
}
for address in emails:
    if address.endswith("@alueducation.com"):
        alu_counts["Official"] +=1
    elif address.endswith("@alumni.alueducation.com"):
        alu_counts["Alumni"] +=1
    elif address.endswith("@si.alueducation.com"):
        alu_counts["SI"] +=1
    else:
        alu_counts["Other"] +=1
    for address in emails:
        local, domain = address.split("@", 1)
        if len(local) <=2:
            masked_local = local[0] + "*"
        else:
            masked_local = local[0] + "*" * (len(local) - 2) + local[-1]
        masked_emails.append(f"{masked_local}@{domain}")    
#using regex for credit card number where there's four groups of four digits
credit = r"\b(?:\d{4}[ -]){3}\d{4}\b"
credits = re.findall(credit, text)
#implimenting credit cards privacy
masked_cards = []
for card in credits:
    masked_cards.append("****-****-****-" + card[-4:])
# currency amounts in usd formats
currency = r"\$\s?[0-9]{1,3}(?:,[0-9]{3})*(?:\.[0-9]{2})?\b"
currencies = re.findall(currency, text)
#phone number regex that allows all phone numbers
phone = r"\b(?:\+\d{1,3}[-.\s]?)?\(?\d{1,4}\)?\d{1,4}[-.\s]?\d{1,9}\b"
phones = re.findall(phone, text)

results = {
    "emails": masked_emails,
    "phone": phones,
    "currency": currencies,
    "credit_cards": masked_cards,
    "validation": {
        "status": "completed",
        "external_text_executed": False
    }
}
with open("output/sample-output.json", "w",) as file:
    json.dump(results, file, indent=4)

print(f"Extraction completed, please check output/sample-output.json for saved results.")