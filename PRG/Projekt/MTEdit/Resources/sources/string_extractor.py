import re
pattern = re.compile('L\["[^\]]+"\]')

code = open('mtedit.py')

f = open("Locales/en.json", "w")
f.write("[")

for i, line in enumerate(code):
    for match in re.finditer(pattern, line):
        f.write("\n   " + match.group()[2:-1] + ",")

f.seek(f.tell() - 1)

f.write("\n]\n")
f.close()
code.close()