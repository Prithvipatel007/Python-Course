alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO 1 - Combine the encrypt and decrypt functions into a single function called caesar
def caesar(direction, text, shift):
    end_text = ""

    for letter in text:
        pos = alphabet.index(letter)

        if(direction == "encode"):
            new_pos = pos + shift
            # loop back to the first alphabet
            if(new_pos > len(alphabet)):
                new_letter = alphabet[new_pos % len(alphabet)]
            else:
                new_letter = alphabet[new_pos]
            end_text += new_letter

        elif(direction == "decode"):
            new_pos = pos - shift
            # loop back to the last alphabet
            if(new_pos < 0):
                new_letter = alphabet[new_pos % len(alphabet)]
            else:
                new_letter = alphabet[new_pos]
            end_text += new_letter
        
        else:
            print("Invalid direction, cannot process message")

    print(f"The output message is {end_text}")



# TODO 2 - Call the caesar function, passing over the text, shift and direction values, Get rid of the if else decision statement
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(direction=direction, text=text, shift=shift)

