from CYK import CYK

cur_start = "S"

cur_grammar = {
    cur_start: ["AB"],
    "A": ["a", "b", "c", "d", "e", "f"],
    "B": ["CD", "a"],
    "C": ["="],
    "D": ["EF", "a", "b", "c", "d", "e", "f", "0", "1", "HI", "JD", "AK", "HK"],
    "E": ["("],
    "F": ["DG", "DM"],
    "G": [")"],
    "H": ["0", "1"],
    "I": ["HI", "HK", "HD"],
    "J": ["-"],
    "O": ["*", "/", "%", "+", "-"],
    "K": ["OD"],
    "M": ["GN"],
    "N": ["OD"],
}

cyk = CYK(cur_grammar, cur_start)


def test_my_grammar_1():

    cur_word = "a=a*b"

    assert cyk.checkWord(cur_word)


def test_my_grammar_2():

    cur_word = "b=(a*1010)"

    assert cyk.checkWord(cur_word)


def test_my_grammar_3():

    cur_word = "c=a*111111111111111*a"

    assert cyk.checkWord(cur_word)


def test_my_grammar_4():

    cur_word = "d=(b*1)*c"

    assert cyk.checkWord(cur_word)


def test_my_grammar_5():

    cur_word = "e=a*(d*e)*f"

    assert cyk.checkWord(cur_word)


def test_my_grammar_6():

    cur_word = "f=a*(a)*a"

    assert cyk.checkWord(cur_word)


def test_my_grammar_7():

    cur_word = "a=(a*-1010)"

    assert cyk.checkWord(cur_word)


def test_my_grammar_8():

    cur_word = "b=a*-111111111111111*a"

    assert cyk.checkWord(cur_word)


def test_my_grammar_9():

    cur_word = "c=(b*1)*c"

    assert cyk.checkWord(cur_word)


def test_my_grammar_10():

    cur_word = "d=1+(a-(b*c)/f)"

    assert cyk.checkWord(cur_word)


def test_my_grammar_11():

    cur_word = "e=a*-(d*e)*f"

    assert cyk.checkWord(cur_word)


def test_my_grammar_12():

    cur_word = "f=a*((-a))*a"

    assert cyk.checkWord(cur_word)


def test_my_grammar_13():

    cur_word = "a=a--b"

    assert cyk.checkWord(cur_word)


def test_my_grammar_14():

    cur_word = "b=a**b"

    assert not cyk.checkWord(cur_word)


def test_my_grammar_15():

    cur_word = "c=abc"

    assert not cyk.checkWord(cur_word)


def test_my_grammar_16():

    cur_word = "d=a*-((de)*f"

    assert not cyk.checkWord(cur_word)


def test_my_grammar_17():

    cur_word = "e=a*(-a))*a"

    assert not cyk.checkWord(cur_word)


def test_my_grammar_18():

    cur_word = "a+b"

    assert not cyk.checkWord(cur_word)
