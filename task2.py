import re

def extract_info(infile, outfile):
    with open(infile, 'r') as fi:
        data = fi.read()

    birth_date_pattern = r'\b\d{2}.\d{2}.\d{4}\b'
    phone_pattern = r'\+\d{12}'
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    birth_dates = re.findall(birth_date_pattern, data)
    phones = re.findall(phone_pattern, data)
    emails = re.findall(email_pattern, data)

    with open(outfile, 'w') as fo:
        fo.write("Дні народження:\n")
        for date in birth_dates:
            fo.write(date + "\n")

        fo.write("Телефони:\n")
        for phone in phones:
            fo.write(phone + "\n")

        fo.write("Emails:\n")
        for email in emails:
            fo.write(email + "\n")

extract_info("test.txt", "test1.txt")
