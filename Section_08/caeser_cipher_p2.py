alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(Plain_text, shift):
    cipher_text = ""
    for letter in Plain_text:
        pos = alphabet.index(letter)
        new_pos = pos + shift
        
        # loop back to the first alphabet
        if(new_pos > len(alphabet)):
            new_letter = alphabet[new_pos % len(alphabet)]
        else:
            new_letter = alphabet[new_pos]

        cipher_text += new_letter

    print(cipher_text)
# TODO - 1- Create decrypt function tat takes the text and shift as inputs
# Inside the decrypt function, shift each letter of the text in the backward direction in the alphabet list and print the decrypted text
def decrypt(cipher_text, shift):
    plain_text = ""
    for letter in cipher_text:
        pos = alphabet.index(letter)
        new_pos = pos - shift

        # loop back to the last alphabet
        if(new_pos < 0):
            new_letter = alphabet[new_pos % len(alphabet)]
        else:
            new_letter = alphabet[new_pos]
        
        plain_text += new_letter

    print(plain_text)



# TODO 2 - Check if the user wanted to encrypt or decrypt the message by checking the direction variable. Then call the correct function based on that direction variable. You should be able to test the code to encrypt and decrypt a message
if direction == "encode":
    encrypt(
        Plain_text = text, 
        shift = shift
    )
elif direction == "decode":
    decrypt(
        cipher_text=text,
        shift=shift
    )
else:
    print("Please enter valid direction")

