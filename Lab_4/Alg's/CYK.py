class CYK:
    _word_length = 0

    def __init__(self, grammar, start):
        self._grammar = grammar
        self._start = start
        self._table = [[{}]]  # Формат хранения: [индекс][индекс][ключ(нетерминальный символ)-значение]

    def checkWord(self, word):
        self._word_length = len(word)
        self.init_step(word)
        return self.check_table()

    def init_step(self, word):
        self._table = [[{}  # r
                        for _ in range(self._word_length + 1)]  # n
                       for _ in range(self._word_length + 1)]   # n

        for j in range(1, len(word) + 1):
            for key, value in self._grammar.items():
                if word[j - 1] in value:
                    self._table[1][j][key] = True

        self.main_action(word)

    def main_action(self, word):

        for i in range(2, len(word) + 1):
            for j in range(1, len(word) - i + 2):
                for k in range(1, i):

                    for key, value in self._grammar.items():
                        for prod in value:
                            if len(prod) == 1:
                                continue

                            if prod[0] in self._table[k][j] and \
                                    prod[1] in self._table[i - k][j + k]:
                                if self._table[k][j][prod[0]] and \
                                        self._table[i - k][j + k][prod[1]]:
                                    self._table[i][j][key] = True

    def check_table(self):
        if 'S' in self._table[self._word_length][1]:
            if self._table[self._word_length][1]['S']:
                return True
        return False


if __name__ == "__main__":
    cur_start = "S"

    cur_grammar = {
        "S": ["AB"],
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
        "O": ["*", "/", "%"],
        "P": ["+", "-"],
        "K": ["OD", "PD"],
        "M": ["GN"],
        "N": ["OD"],
    }

    cur_word = "a=b+c"

    a = CYK(cur_grammar, cur_start)

    print(a.checkWord(cur_word))
