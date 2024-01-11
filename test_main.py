import main
from cipher.caesar import CaesarCipher
from art import logo


def test_encode(capfd, monkeypatch):
    inputs = ["encode", "Hello 2 World$ ", "5", "no"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    cipher = CaesarCipher()
    main.run(cipher)
    out, err = capfd.readouterr()
    assert out == f"{logo}\nHere's the encoded result: Mjqqt 2 Btwqi$ \n"


def test_encode_empty_string(capfd, monkeypatch):
    inputs = ["encode", "", "5", "no"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    cipher = CaesarCipher()
    main.run(cipher)
    out, err = capfd.readouterr()
    assert out == f"{logo}\nHere's the encoded result: \n"


def test_encode_one_character(capfd, monkeypatch):
    inputs = ["encode", "H", "5", "no"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    cipher = CaesarCipher()
    main.run(cipher)
    out, err = capfd.readouterr()
    assert out == f"{logo}\nHere's the encoded result: M\n"


def test_encode_large_shift_amount(capfd, monkeypatch):
    inputs = ["encode", "I like chemistry $%6", "36", "no"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    cipher = CaesarCipher()
    main.run(cipher)
    out, err = capfd.readouterr()
    assert out == f"{logo}\nHere's the encoded result: S vsuo mrowscdbi $%6\n"


def test_decode(capfd, monkeypatch):
    inputs = ["decode", "Mjqqt 2 Btwqi$ ", "5", "no"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    cipher = CaesarCipher()
    main.run(cipher)
    out, err = capfd.readouterr()
    assert out == f"{logo}\nHere's the decoded result: Hello 2 World$ \n"


def test_decode_empty_string(capfd, monkeypatch):
    inputs = ["decode", "", "5", "no"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    cipher = CaesarCipher()
    main.run(cipher)
    out, err = capfd.readouterr()
    assert out == f"{logo}\nHere's the decoded result: \n"


def test_decode_one_character(capfd, monkeypatch):
    inputs = ["decode", "H", "5", "no"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    cipher = CaesarCipher()
    main.run(cipher)
    out, err = capfd.readouterr()
    assert out == f"{logo}\nHere's the decoded result: C\n"


def test_decode_large_shift_amount(capfd, monkeypatch):
    inputs = ["decode", "S vsuo mrowscdbi $%6", "36", "no"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    cipher = CaesarCipher()
    main.run(cipher)
    out, err = capfd.readouterr()
    assert out == f"{logo}\nHere's the decoded result: I like chemistry $%6\n"


def test_encode_and_decode(capfd, monkeypatch):
    inputs = ["encode", "Hello 2 World$ ", "5", "yes", "decode", "Mjqqt 2 Btwqi$ ", "5", "no"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    cipher = CaesarCipher()
    main.run(cipher)
    out, err = capfd.readouterr()
    assert out == f"{logo}\nHere's the encoded result: Mjqqt 2 Btwqi$ \nHere's the decoded result: Hello 2 World$ \n"


def test_wrong_input(capfd, monkeypatch):
    inputs = ["wrong_input"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    cipher = CaesarCipher()
    main.run(cipher)
    out, err = capfd.readouterr()
    assert out == f"{logo}\nYou chose a wrong direction. Try again.\n"


def test_wrong_input_for_shift_amount_does_not_fail(capfd, monkeypatch):
    inputs = ["encode", "Hello 2 World$", "test", "5", "no"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    cipher = CaesarCipher()
    main.run(cipher)
    out, err = capfd.readouterr()
    assert out == f"{logo}\nHere's the encoded result: Mjqqt 2 Btwqi$\n"
