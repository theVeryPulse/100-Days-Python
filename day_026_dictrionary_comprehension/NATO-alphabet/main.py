# This program takes words and converts them into their corresponding nato codes
# SKILLS: dictionary comprehension, pandas
# Difficulty: easy

import pandas as pd
# pandas method: iterrows(), returns (row_index, row_content)

# Create a dictionary in this format: {"A": "Alfa", "B": "Bravo" ... "Z": "Zulu"}
content = pd.read_csv('nato_phonetic_alphabet.csv')
nato_ab = {row.letter: row.code for (index, row) in content.iterrows()}
# print(nato_ab)

# Create a list of the phonetic code words from words that users input.
while True:
    word = input("What word would you like to convert?\n")
    converted = []
    for char in word:
        try:
            char_code = nato_ab[char.upper()]
        except Exception:
            converted.append(char)
        else:
            converted.append(char_code)
    print(converted)





