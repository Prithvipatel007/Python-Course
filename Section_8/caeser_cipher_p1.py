alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO - 1 - Create a function called encrypt that takes text and shift as input
# Inside the encrypt function, shift each letter of the text forward in the alphabet by th eshift amount and print he encrypted text
def encrypt(Plain_text, shift):
    cipher_text = ""
    for letter in Plain_text:
        pos = alphabet.index(letter)
        new_pos = pos + shift
        
        if(new_pos > len(alphabet)):
            new_letter = alphabet[new_pos % len(alphabet)]
        else:
            new_letter = alphabet[new_pos]

        cipher_text += new_letter

    print(cipher_text)

# TODO - 2 - Call the encrypt function and pass in the user input. You should be able to test the code and encrypt the message
encrypt(
    Plain_text = text, 
    shift = shift
)