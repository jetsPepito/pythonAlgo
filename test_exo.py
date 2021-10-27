from exo import addString, averageLen, dico, fibo, firstUniqueChar, get30, getMax, inverseInt, palindrome, perfectSquare


def test_get30():
    T = [0,5,3,2,12,8,7,4,3]
    assert get30(T) == (5,3,2)

def test_palindrome():
    word = "test"
    assert not palindrome(word)

def test_palindrome_good():
    word = "kayak"
    assert palindrome(word)

def test_getMax():
    T = [0,2,5,25,-2,-12]
    assert getMax(T) == 25

def test_inverseInt():
    val = 1234
    assert inverseInt(val) == 4321

def test_invereIntNeg():
    val = -1234
    assert inverseInt(val) == -4321

def test_averageLen():
    text = "Même les phrases avec des c....aractères de la langue française peuvent être utilisées."
    assert averageLen(text) == 5.38

def test_fibo():
    assert fibo(4) == 5

def test_addString():
    assert addString("100", "-5") == "95"

def test_dico():
    assert dico([1,2,5,8,12,34,96,102,110,112], 110) == 8

def test_firstUniqueChar():
    assert(firstUniqueChar("Europe")) == "u"

def test_perfect_square():
    assert(perfectSquare(3,15)) == [4,9]