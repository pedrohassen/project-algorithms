from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(3, 'abcdef')
    assert encrypt_message("abcdef", 2) == "fedc_ba"
    assert encrypt_message("carro", 9) == "orrac"
