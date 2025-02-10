# 5 Winner takes it all brukar det ju heta, men nu ska vi försöka ge lite
# heder åt alla andrapristagare. Formulera testfall för en funktion som hittar näst största talet i en lista!
# Returnerar det nästa största talet i listan
# Returnerar None om det inte finns något
# Om det är delad förstaplats så returneras det talet
from ..src.winner import find_2nd_max

def test__find_2nd_max__returns_2nd_max():
    testdata = [1, 3, 2, 4]
    expected = 3
    actual = find_2nd_max(testdata)
    assert actual == expected

def test__find_2nd_max__None_when_no_2nd_max():
    # Tom lista eller lista med bara 1 element - har inget näst största värde
    testdata = []
    expected = None
    actual = find_2nd_max(testdata)
    assert actual == expected

    assert find_2nd_max([11]) == None


# TODO: testa delad förstaplats
# TODO: testa vad funktionen ska göra om input inte är en lista!
