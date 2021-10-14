from crypt import Coder

def test_coder():
    assert Coder.coder("СУПЕР СЕКРЕТНОЕ СООБЩЕНИЕ", "ЛАДЬЯ") == "УСТСЕПЕНОНС Е ЩЕКООИРРЕБЕ"