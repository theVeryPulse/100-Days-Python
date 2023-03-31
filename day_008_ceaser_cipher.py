alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
#encode function
def encrypt(plain_text,shift_amount):
    message = ""
    for letter in plain_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            index += shift_amount
            if index >= 26:
                index -= 26
            message += alphabet[index]
        else:
            message += letter
    return (message)

#decode function
def decrypt(encrypted,shift_amount):
    message = ""
    for letter in encrypted:
        if letter in alphabet:
            index = alphabet.index(letter)
            index -= shift_amount
            message += alphabet[index]
        else:
            message += letter
    return (message)

def ceaser(text,number,direction):
    if direction == "encode":
        print(encrypt(text,number))
    else:
        print(decrypt(text,number))

status = "yes"
while status != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift >= 26:
        shift = shift % 26
        #print(shift)
    ceaser(text,shift,direction)
    status = input("Do you wish to keep going? Inpuy 'yes' or 'no': ").lower()