import re


def parse_dates(text):
    pattern = r"(?:^|\D)(\d{2}/\d{2}/\d{4})(?:\D|$)"
    dates = re.findall(pattern, text)
    print('1 - date:', dates)

    pattern = r"(?:^|\D)(\d{2}-\d{2}-\d{4})(?:\D|$)"
    dates = re.findall(pattern, text)
    print('1 - date:', dates)

    pattern = r"(?:^|\D)(\d{4}\.\d{2}\.\d{2})(?:\D|$)"
    dates = re.findall(pattern, text)
    print('1 - date:', dates)

    pattern = r"(?:^|\D)(\d{4}/\d{2}/\d{2})(?:\D|$)"
    dates = re.findall(pattern, text)
    print('1 - date:', dates)


def parse_dates_with_words(text):
    pattern = r"((?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4})"
    dates = re.findall(pattern, text)
    print('2 - date with words:', dates)


def parse_phone_numbers(text):
    pattern = r"\(\d{3}\)\s\d{3}-\d{4}"
    phoneNumber = re.findall(pattern, text)
    print('3 - phone numbers:', phoneNumber)

    pattern = r"\s(\d{3}[\.\-]\d{3}[\.\-]\d{4})"
    phoneNumber = re.findall(pattern, text)
    print('3 - phone numbers:', phoneNumber)

    pattern = r"\+[\d\-\s]*\d"
    phoneNumber = re.findall(pattern, text)
    print('4 - phone numbers:', phoneNumber)


def parse_emails(text):
    pattern = r"[a-zA-Z\-_\.\+\d]+@[a-zA-Z\-_\.\+\d]+"
    emails = re.findall(pattern, text)
    print('5, 6 - emails:', emails)


def parse_URLs(text):
    pattern = r"(?:(?:https?|ftp)://|www\.)[\w\./\-?=#]+"
    URLs = re.findall(pattern, text)
    print('7, 8 - URLs:', URLs)


def parse_hexadecimal(text):
    pattern = r"(?:0x|#)[A-F\d]+"
    hexadecimal = re.findall(pattern, text)
    print('9, 10 - hexadecimal:', hexadecimal)


def parse_rgb(text):
    pattern = r"rgb\((?:[\d\.]+,\s){2}[\d\.]+\)|rgba\((?:[\d\.]+,\s){3}[\d\.]+\)"
    rgb = re.findall(pattern, text)
    print('11 - RGB:', rgb)


def parse_social_security_numbers(text):
    pattern = r"(?<!\w)\d{3}[\- ]?\d{2}[\- ]?\d{4}(?!\w)"
    socialSecurityNumbers = re.findall(pattern, text)
    print('12, 13 - Social security numbers:', socialSecurityNumbers)


def parse_sentences(text):
    pattern = r"[A-Z][a-zA-Z ,]+\."
    sentences = re.findall(pattern, text)
    print('14 - Sentences:', sentences)


def parse_special_symbols_and_numbers(text):
    pattern = r"1234567890|!@#\$%\^&\*\(\)_\+-=\[\]\{\}\|;':\"|\./<>\?|3\.14159|42|\-273.15"
    specials = re.findall(pattern, text)
    print('15 - Special symbols and numbers:', specials)


if __name__ == '__main__':
    f = open("data.txt", "r")
    text = f.read()

    parse_dates(text)
    parse_dates_with_words(text)
    parse_phone_numbers(text)
    parse_emails(text)
    parse_URLs(text)
    parse_hexadecimal(text)
    parse_rgb(text)
    parse_social_security_numbers(text)
    parse_sentences(text)
    parse_special_symbols_and_numbers(text)
