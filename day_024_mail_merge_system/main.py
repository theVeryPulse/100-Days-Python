# This is a mail merge system
# for each name in './Input/Letters/starting_letter.txt'
# the [name] placeholder is replaced with names from './Input/Names/invited_names.txt'
# letters are saved in './Output/ReadyToSend'
# SKILLS: read/write files, directory

# useful links
# 1 https://www.w3schools.com/python/ref_file_readlines.asp
# 2 https://www.w3schools.com/python/ref_string_replace.asp
# 3 https://www.w3schools.com/python/ref_string_strip.asp

# read the letter template
with open('./Input/Letters/starting_letter.txt', 'r') as file:
    letter_template = file.read()

# read the list of names
with open('./Input/Names/invited_names.txt', 'r') as file:
    name_list = file.readlines()

# for each name, write a letter
for name in name_list:
    name = name.strip()
    new_letter = letter_template.replace("[name]", F"{name}")
    print(new_letter)
    with open(F'./Output/ReadyToSend/letter_for_{name}', 'w') as letter:
        letter.write(new_letter)


