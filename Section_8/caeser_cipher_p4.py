from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
    end_text = ""

    # TODO - 2- What happens if the user enters a number/symbol/space?
    # If the character is not in the list, the character remains as it is and move to the next character
    for letter in text:
        if(letter in alphabet):
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
            end_text += letter

    print(f"The output message is {end_text}")

# TODO - 3 - Can you figure out a way to ask the user if they want to restart cipher program

#TODO - 1- Import and print the logo from art.py when the program starts
print(logo)
restart = True

while(restart == True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction=direction, text=text, shift=shift)

    ans = input("Do you want to restart the cipher program? Type yes to restart, no to exit : ").lower()
    if(ans == "no"):
        restart = False
        print("Good bye! Cya later!")



