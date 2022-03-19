import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ', '0','1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ', '0','1', '2', '3', '4', '5', '6', '7', '8', '9']


def caesar(in_text, shift_amount, direction):
    out_text = ""
    for letter in in_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = position + shift_amount
            elif direction == "decode":
                new_position = position - shift_amount
            else:
                print("Invalid input for direction.")
                return
            new_letter = alphabet[new_position]
            out_text += new_letter
        else:
            out_text +=  letter

    print(f"The {direction}d text is:  {out_text}")


print(art.logo)
again = "y"
while again == "y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = int(shift % (len(alphabet) / 2))
    if shift == 0:
        redo = True
        while redo:
            print("The selected shift amount will not encode or decode your message.")
            shift = int(input("Please enter a different shift value:\n"))
            shift = int(shift % (len(alphabet) / 2))
            if shift != 0:
                redo = False
    caesar(text, shift, direction)
    again = input("Type 'y' to continue.")