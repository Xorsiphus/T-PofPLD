import sys

EOI = 0
NUM = 1
VAR = 2
NEGATIVE = 3
ADDITIVE = 4
MULTI = 5
EQUAL = 6
LB = 20
RB = 21
SEPARATOR = 13
UNKNOWN = -1

TOKEN = 0
LEXEME = 1

SUCCESS = 0
ERROR = -1

MATCHING_DICT = {
    NUM: ['0', '1', '2', '3', '4',
          '5', '6', '7', '8', '9'],
    VAR: ['a', 'b', 'c', 'd', 'e', 'f'],
    NEGATIVE: ['!'],
    ADDITIVE: ['+', '-'],
    MULTI: ['*', '/', '%'],
    LB: ['('],
    RB: [')'],
    EQUAL: ['='],
    SEPARATOR: [';'],
    EOI: ['$']
}


class RDParser:

    input_index = 0
    str_for_parse = ''

    @staticmethod
    def get_next_token():
        temp_token = EOI

        if RDParser.str_for_parse[RDParser.input_index] in MATCHING_DICT[NUM]:
            temp_token = NUM
        elif RDParser.str_for_parse[RDParser.input_index] in MATCHING_DICT[VAR]:
            temp_token = VAR
        elif RDParser.str_for_parse[RDParser.input_index] in MATCHING_DICT[LB]:
            temp_token = LB
        elif RDParser.str_for_parse[RDParser.input_index] in MATCHING_DICT[RB]:
            temp_token = RB
        elif RDParser.str_for_parse[RDParser.input_index] in MATCHING_DICT[NEGATIVE]:
            temp_token = NEGATIVE
        elif RDParser.str_for_parse[RDParser.input_index] in MATCHING_DICT[MULTI]:
            temp_token = MULTI
        elif RDParser.str_for_parse[RDParser.input_index] in MATCHING_DICT[ADDITIVE]:
            temp_token = ADDITIVE
        elif RDParser.str_for_parse[RDParser.input_index] in MATCHING_DICT[EQUAL]:
            temp_token = EQUAL
        elif RDParser.str_for_parse[RDParser.input_index] in MATCHING_DICT[SEPARATOR]:
            temp_token = SEPARATOR
        elif len(RDParser.str_for_parse) > RDParser.input_index + 1:
            temp_token = UNKNOWN

        if temp_token == UNKNOWN:
            RDParser.raise_error(Exception('Unknown input symbol!'))

        if temp_token != EOI:
            RDParser.input_index += 1
            return temp_token, RDParser.str_for_parse[RDParser.input_index - 1]
        return temp_token, ''

    @staticmethod
    def token_rollback():
        RDParser.input_index -= 1

    @staticmethod
    def raise_error(exc=Exception('Wrong input!')):
        print('Rejected!')
        raise exc

    @staticmethod
    def parse(str_for_parse):

        RDParser.input_index = 0
        RDParser.str_for_parse = str_for_parse + '$'

        if RDParser.start() == 0 and len(str_for_parse) == RDParser.input_index + 1:
            print('Accepted!')
            return True
        else:
            print('Rejected!')
            return False

    @staticmethod
    def start():
        res = SUCCESS
        token = RDParser.get_next_token()

        if token[TOKEN] == VAR:
            res += RDParser.b_func()
            res += RDParser.c_func()
            res += RDParser.d_func()
            if RDParser.get_next_token()[TOKEN] != SEPARATOR:
                RDParser.raise_error()
                # res += ERROR
            res += RDParser.e_func()
        else:
            RDParser.raise_error()
            # res += ERROR
        return res

    @staticmethod
    def b_func():
        token = RDParser.get_next_token()
        if token[TOKEN] == VAR:
            return SUCCESS
        else:
            RDParser.token_rollback()
            return SUCCESS

    @staticmethod
    def c_func():
        token = RDParser.get_next_token()
        if token[TOKEN] == EQUAL:
            return SUCCESS
        else:
            RDParser.raise_error()
            # return ERROR

    @staticmethod
    def d_func():
        res = SUCCESS
        token = RDParser.get_next_token()
        if token[TOKEN] == LB:
            res += RDParser.d_func()
            if RDParser.get_next_token()[TOKEN] != RB:
                RDParser.raise_error()
                # res += ERROR
            res += RDParser.f_func()
        elif token[TOKEN] == VAR:
            res += RDParser.b_func()
            res += RDParser.f_func()
        elif token[TOKEN] == NUM and token[LEXEME] == '1':
            res += RDParser.g_func()
            res += RDParser.f_func()
        elif token[TOKEN] == NEGATIVE:
            res += RDParser.d_func()
        else:
            RDParser.raise_error()
            # res += ERROR
        return res

    @staticmethod
    def e_func():
        res = SUCCESS
        token = RDParser.get_next_token()
        if token[TOKEN] == VAR:
            res += RDParser.b_func()
            res += RDParser.c_func()
            res += RDParser.d_func()
            if RDParser.get_next_token()[TOKEN] != SEPARATOR:
                RDParser.raise_error()
                # res += ERROR
            res += RDParser.e_func()
        else:
            RDParser.token_rollback()
        return res

    @staticmethod
    def f_func():
        res = SUCCESS
        token = RDParser.get_next_token()
        if token[TOKEN] == MULTI:
            res += RDParser.d_func()
        elif token[TOKEN] == ADDITIVE:
            RDParser.token_rollback()
            res += RDParser.h_func()
        else:
            RDParser.token_rollback()
        return res

    @staticmethod
    def g_func():
        res = SUCCESS
        token = RDParser.get_next_token()
        if token[TOKEN] == NUM:
            res += RDParser.g_func()
        else:
            RDParser.token_rollback()
            res += SUCCESS
        return res

    @staticmethod
    def h_func():
        res = SUCCESS
        token = RDParser.get_next_token()
        if token[TOKEN] == ADDITIVE:
            res += RDParser.d_func()
        else:
            RDParser.raise_error()
        return res


def main():
    if len(sys.argv) > 1:
        try:
            RDParser.parse(sys.argv[1])
        except Exception as e:
            print(e)
    else:
        temp = input()
        try:
            RDParser.parse(temp)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
