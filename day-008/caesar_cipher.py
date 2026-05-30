def encode(text, shift):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    cipher_text = ''
    for char in text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position + shift) % 26
            cipher_text += alphabets[new_position]
        else:
            cipher_text += char
    print(f"The encoded text is {cipher_text}")

def decode(text, shift):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    deciphered_text = ''
    for char in text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position - shift) % 26
            deciphered_text += alphabets[new_position]
        else:
            deciphered_text += char
    print(f"The decoded text is {deciphered_text}")


backgrnd=''' ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           '''
print()
print(backgrnd)
choice="yes"


while choice!="no":
    choice=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ")
    text=input("Type your message:\n ")
    shift=int(input("Type the shift number:\n "))
    if choice=="encode":
        encode(text,shift)
    elif choice=="decode":
        decode(text,shift)

    choice=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")



print("Goodbye!")
