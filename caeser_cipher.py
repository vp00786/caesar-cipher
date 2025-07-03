alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, direction):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:  # Check if the letter is in the alphabet
            shifted_position = alphabet.index(letter)
            if direction == "encode":
                shifted_position += shift_amount
            elif direction == "decode":
                shifted_position -= shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter  # Keep non-alphabet characters unchanged

    if direction == "encode":
        print(f"Here is the encoded result: {cipher_text}")
    elif direction == "decode":
        print(f"Here is the decoded result: {cipher_text}")

caesar(text, shift, direction)
