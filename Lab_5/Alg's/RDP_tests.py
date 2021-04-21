from recursive_descent_parser import RDParser


def test_my_grammar_1():
    cur_word = "a=a*b;"

    t = False

    try:
        t = RDParser.parse(cur_word)
    except Exception as e:
        _ = e

    assert t


def test_my_grammar_2():
    cur_word = "a=b*(101/cd);"

    t = False

    try:
        t = RDParser.parse(cur_word)
    except Exception as e:
        _ = e

    assert t


def test_my_grammar_3():
    cur_word = "a=b*(1/cd)%1010;"

    t = False

    try:
        t = RDParser.parse(cur_word)
    except Exception as e:
        _ = e

    assert t


def test_my_grammar_4():
    cur_word = "a=b;"

    t = False

    try:
        t = RDParser.parse(cur_word)
    except Exception as e:
        _ = e

    assert t


def test_my_grammar_5():
    cur_word = "a=a*b;b=c+d;"

    t = False

    try:
        t = RDParser.parse(cur_word)
    except Exception as e:
        _ = e

    assert t


def test_my_grammar_6():
    cur_word = "a=a;b=b;c=c;d=!!!d;e=101010100101010;"

    t = False

    try:
        t = RDParser.parse(cur_word)
    except Exception as e:
        _ = e

    assert t


def test_my_grammar_7():
    cur_word = "bc=ac+(af*(1010/b)+111)-10;"

    t = False

    try:
        t = RDParser.parse(cur_word)
    except Exception as e:
        _ = e

    assert t


def test_my_grammar_8():
    cur_word = "a=a*b"

    t = False

    try:
        t = RDParser.parse(cur_word)
    except Exception as e:
        _ = e

    assert not t


def test_my_grammar_9():
    cur_word = "a=abc"

    t = False

    try:
        t = RDParser.parse(cur_word)
    except Exception as e:
        _ = e

    assert not t
