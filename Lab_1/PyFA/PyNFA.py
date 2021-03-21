import sys
from enum import Enum

TOTAL_STATES = 3
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


class Input(Enum):
    a = 0
    b = 1


gAcceptedStates = [DFA_STATES.q0, DFA_STATES.q1, DFA_STATES.q3]
gAlphabet = ('a', 'b')
gTransitionTable = [[0] * ALPHABET_CHARCTERS for i in range(TOTAL_STATES)]
gCurrentState = DFA_STATES.q0


def setDFATransitions() -> None:
    gTransitionTable[DFA_STATES.q0.value][Input.a.value] = DFA_STATES.q1
    gTransitionTable[DFA_STATES.q0.value][Input.b.value] = DFA_STATES.q2
    gTransitionTable[DFA_STATES.q1.value][Input.a.value] = DFA_STATES.q1
    gTransitionTable[DFA_STATES.q2.value][Input.a.value] = DFA_STATES.q3
    gTransitionTable[DFA_STATES.q2.value][Input.b.value] = DFA_STATES.q2


def dfa(current_symbol: chr) -> int:
    global gAcceptedStates
    global gCurrentState
    global gTransitionTable

    if current_symbol not in gAlphabet:
        return UNKNOWN_SYMBOL_ERR
 
    old_state = gCurrentState
    try:
        gCurrentState = gTransitionTable[gCurrentState.value][gAlphabet.index(current_symbol)]
    except Exception as e:
        return NOT_REACHED_FINAL_STATE

    print(current_symbol + ": " + str(old_state) + " -> " + str(gCurrentState))  # route info

    if gCurrentState in gAcceptedStates:
        return REACHED_FINAL_STATE

    return NOT_REACHED_FINAL_STATE


if __name__ == "__main__":
    result = REACHED_FINAL_STATE

    setDFATransitions()

    print("Enter a string with 'a' s and 'b's:\nPress Enter Key to stop\n")

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
