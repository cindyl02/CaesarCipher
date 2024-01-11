class CaesarCipher:
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
        'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
        't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    def caesar(self, start_text, shift_amount, cipher_direction):
        text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for char in start_text:
            if char.isalpha():
                position = self.alphabet.index(char.lower())
                new_position = (position + shift_amount) % 26
                if char.isupper():
                    text += self.alphabet[new_position].upper()
                else:
                    text += self.alphabet[new_position]
            else:
                text += char
        return f"Here's the {cipher_direction}d result: {text}"
