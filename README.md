I. ALU Regex Data Extraction system 

An automated Python-based data extraction and masking pipeline designed to parse raw unstructured text file "input/raw-text.txt" and safely extract validated entities (emails, phone numbers, transaction currencies, and credit card number) into structrued JSON format "output/sample-output.json"

II. Key features
    - ALU domain validation: classifies and validates domain specific institutional emails ('@alueducation.com', '@alumni.alueducation.com', and '@si.alueducation.com').
    -Data privacy and masking: 
        --Emails: local-part username characters are partially masked (eg: 'd*****a@alueducation.com')
        --credit cards: standard 16-digit cards are obfuscated, preserving only the final 4 digits (eg: '****-****-****-1234')
    -Structured JSON export: formats extracted entities and validation metadata into clean, indented JSON.



III. Requirements:

    - Python: 3.8+(No external third party dependencies required; uses standard libraries re, json and pathlib)

IV. Structure:

alu-regex-data-extraction_{GithubUsername}/
├── input/
│   └── raw-text.txt
├── src/
│   └── main.py
├── output/
│   └── sample-output.json
└── README.md

V. How to run:
    1. Place raw data: ensure your target unstructured text file is saved at "input/raw-text.txt"
    2. Execute the script from the root directory "python3 src/main.py"
    3. Open "output/sample-output.json" to inspect the extracted and masked datasets.