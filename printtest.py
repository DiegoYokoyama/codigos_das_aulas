import re
pattern = r"abc"
string = "abcdef"

match = re.match(pattern, string)
if match:
    print("Correspondência encontrada:", match.group())
else:
    print("Nenhuma correspondência encontrada.")