from art import logo
from cipher.caesar import CaesarCipher


def get_direction():
    return input('Type "encode" to encrypt, type "decode" to decrypt: ')


def get_message():
    return input("Type your message: ")


def get_shift():
    success = False
    while not success:
        try:
            return int(input("Type the shift number: "))
        except ValueError:
            pass

def get_run_again():
    return input('Type "yes" to continue or "no": ').lower()


def run(cipher):
    print(logo)
    should_continue = True
    while should_continue:
        direction = get_direction()
        if direction != "encode" and direction != "decode":
            print("You chose a wrong direction. Try again.")
            break
        text = get_message()
        shift = get_shift()
        print(cipher.caesar(text, shift % 26, direction))
        run_again = get_run_again()
        if run_again == "no":
            should_continue = False


if __name__ == '__main__':
    cipher = CaesarCipher()
    run(cipher)
