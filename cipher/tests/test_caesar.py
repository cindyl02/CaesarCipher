from cipher.caesar import CaesarCipher


def test_encode_empty_string():
    caesar_cipher = CaesarCipher()
    assert caesar_cipher.caesar("", 5, "encode") == "Here's the encoded result: "


def test_encode_by_small_shift_amount():
    caesar_cipher = CaesarCipher()
    assert caesar_cipher.caesar("hello33", 5, "encode") == "Here's the encoded result: mjqqt33"


def test_encode_by_large_shift_amount():
    caesar_cipher = CaesarCipher()
    assert caesar_cipher.caesar("I like chemistry $%6", 36,
                                "encode") == "Here's the encoded result: S vsuo mrowscdbi $%6"


def test_encode_by_zero_shift():
    caesar_cipher = CaesarCipher()
    assert caesar_cipher.caesar("hello33", 0, "encode") == "Here's the encoded result: hello33"


def test_decode_empty_string():
    caesar_cipher = CaesarCipher()
    assert caesar_cipher.caesar("", 5, "decode") == "Here's the decoded result: "


def test_decode_by_small_shift_amount():
    caesar_cipher = CaesarCipher()
    assert caesar_cipher.caesar("W gsbr gsqfsh asggousg", 14,
                                "decode") == "Here's the decoded result: I send secret messages"


def test_decode_by_large_shift_amount():
    caesar_cipher = CaesarCipher()
    assert caesar_cipher.caesar("oyws&123^", 90, "decode") == "Here's the decoded result: cmkg&123^"


def test_decode_by_zero_shift():
    caesar_cipher = CaesarCipher()
    assert caesar_cipher.caesar("oyws&123^", 0, "decode") == "Here's the decoded result: oyws&123^"
