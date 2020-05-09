import json

with open("Locales/lang.json") as json_file:
    lang = json.load(json_file)

with open("Locales/en.json") as json_file:
    en = {}
    en_tmp = json.load(json_file)
    for item in en_tmp:
        en[item] = item

if lang["default"] != "en":
    with open("Locales/" + lang[lang["default"]]["file"]) as json_file:
        language = json.load(json_file)
else:
    language = en

print(language["car"])