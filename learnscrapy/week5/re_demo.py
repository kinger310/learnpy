import re


# m = re.search(r'Item[\s]*1A.*?(.*?Item[\s]*1B)', m.group(1), re.I | re.S)
# return m.group(1)
# text = extract_10k_item1a(m.group(1))
def extract_10k_item1a(text):
    m = re.search(r'Item[\s]*1A.*?(.*?Item[\s]*1B)', text, re.I | re.S)
    if m:
        return extract_10k_item1a(m.group(1))
    else:
        return text

if __name__ == '__main__':
    text = 'Item 1A \nblah blah \nItem 1A \nblah blah \nItem 1A \nblah blah \nItem 1A \nkey points\nItem 1B'
    s = extract_10k_item1a(text)
    print(s)
