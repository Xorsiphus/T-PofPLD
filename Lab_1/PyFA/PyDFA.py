import sys
from enum import Enum

TOTAL_STATES = 15
FINAL_STATES = 1
ALPHABET_CHARCTERS = 2

UNKNOWN_SYMBOL_ERR = 0
NOT_REACHED_FINAL_STATE = 1
REACHED_FINAL_STATE = 2


class DFA_STATES(Enum):
    q0 = 0
    q1 = 1
    q2 = 2
    q3 = 3
    q4 = 4
    q5 = 5
    q6 = 6
    q7 = 7
    q8 = 8
    q9 = 9
    q10 = 10
    q11 = 11
    q12 = 12
    q13 = 13
    q14 = 14


class Input(Enum):
    zero = 0
    one = 1


gAcceptedStates = [DFA_STATES.q0.value]
gAlphabet = ('0', '1')
gTransitionTable = [[0] * ALPHABET_CHARCTERS for i in range(TOTAL_STATES)]
gCurrentState = DFA_STATES.q0.value


def setDFATransitions() -> None:
    gTransitionTable[DFA_STATES.q0.value][Input.zero.value] = DFA_STATES.q1.value
    gTransitionTable[DFA_STATES.q0.value][Input.one.value] = DFA_STATES.q5.value
    gTransitionTable[DFA_STATES.q1.value][Input.zero.value] = DFA_STATES.q2.value
    gTransitionTable[DFA_STATES.q1.value][Input.one.value] = DFA_STATES.q6.value
    gTransitionTable[DFA_STATES.q2.value][Input.zero.value] = DFA_STATES.q3.value
    gTransitionTable[DFA_STATES.q2.value][Input.one.value] = DFA_STATES.q7.value
    gTransitionTable[DFA_STATES.q3.value][Input.zero.value] = DFA_STATES.q4.value
    gTransitionTable[DFA_STATES.q3.value][Input.one.value] = DFA_STATES.q8.value
    gTransitionTable[DFA_STATES.q4.value][Input.zero.value] = DFA_STATES.q0.value
    gTransitionTable[DFA_STATES.q4.value][Input.one.value] = DFA_STATES.q9.value
    gTransitionTable[DFA_STATES.q5.value][Input.zero.value] = DFA_STATES.q6.value
    gTransitionTable[DFA_STATES.q5.value][Input.one.value] = DFA_STATES.q10.value
    gTransitionTable[DFA_STATES.q6.value][Input.zero.value] = DFA_STATES.q7.value
    gTransitionTable[DFA_STATES.q6.value][Input.one.value] = DFA_STATES.q11.value
    gTransitionTable[DFA_STATES.q7.value][Input.zero.value] = DFA_STATES.q8.value
    gTransitionTable[DFA_STATES.q7.value][Input.one.value] = DFA_STATES.q12.value
    gTransitionTable[DFA_STATES.q8.value][Input.zero.value] = DFA_STATES.q9.value
    gTransitionTable[DFA_STATES.q8.value][Input.one.value] = DFA_STATES.q13.value
    gTransitionTable[DFA_STATES.q9.value][Input.zero.value] = DFA_STATES.q5.value
    gTransitionTable[DFA_STATES.q9.value][Input.one.value] = DFA_STATES.q14.value
    gTransitionTable[DFA_STATES.q10.value][Input.zero.value] = DFA_STATES.q11.value
    gTransitionTable[DFA_STATES.q10.value][Input.one.value] = DFA_STATES.q0.value
    gTransitionTable[DFA_STATES.q11.value][Input.zero.value] = DFA_STATES.q12.value
    gTransitionTable[DFA_STATES.q11.value][Input.one.value] = DFA_STATES.q1.value
    gTransitionTable[DFA_STATES.q12.value][Input.zero.value] = DFA_STATES.q13.value
    gTransitionTable[DFA_STATES.q12.value][Input.one.value] = DFA_STATES.q2.value
    gTransitionTable[DFA_STATES.q13.value][Input.zero.value] = DFA_STATES.q14.value
    gTransitionTable[DFA_STATES.q13.value][Input.one.value] = DFA_STATES.q3.value
    gTransitionTable[DFA_STATES.q14.value][Input.zero.value] = DFA_STATES.q10.value
    gTransitionTable[DFA_STATES.q14.value][Input.one.value] = DFA_STATES.q4.value


def dfa(current_symbol: chr) -> int:
    global gAcceptedStates
    global gCurrentState
    global gTransitionTable

    if current_symbol not in gAlphabet:
        return UNKNOWN_SYMBOL_ERR

    old_state = gCurrentState
    gCurrentState = gTransitionTable[gCurrentState][gAlphabet.index(current_symbol)]
    print(current_symbol + ": " + str(old_state) + " -> " + str(gCurrentState))  # route info
    if gCurrentState in gAcceptedStates:
        return REACHED_FINAL_STATE

    return NOT_REACHED_FINAL_STATE


if __name__ == "__main__":
    result = REACHED_FINAL_STATE

    setDFATransitions()

    print("Enter a string with '0' s and '1's:\nPress Enter Key to stop\n")

    symbol = sys.stdin.read(1)

    while symbol != '\n':
        result = dfa(symbol)

        if UNKNOWN_SYMBOL_ERR == result:
            print('Unknown symbol error')
            break

        symbol = sys.stdin.read(1)

    if REACHED_FINAL_STATE == result:
        print('Accepted')

    if NOT_REACHED_FINAL_STATE == result:
        print('Rejected')
