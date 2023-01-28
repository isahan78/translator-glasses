import json
from googletrans import Translator

# List of language codes
languages = ['af', 'sq', 'ar', 'hy', 'bn', 'bs', 'bg', 'ca', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'gl', 'de', 'el', 'gu', 'hi', 'hu', 'is', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']

# Creating a list to store the language code and name
lang_list = []

# Iterating through the list of languages
for lang in languages:
    # Creating a dictionary to store the language code and name
    lang_dict = {}
    # Adding the language code and name to the dictionary
    lang_dict["code"] = lang
    lang_dict["name"] = Translator.translate(lang, src='auto', dest='en').text
    # Appending the dictionary to the list
    lang_list.append(lang_dict)

# Serializing the list to a JSON file
with open("languages.json", "w") as outfile:
    json.dump(lang_list, outfile)
