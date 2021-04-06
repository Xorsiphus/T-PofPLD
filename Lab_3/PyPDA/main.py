UNKNOWN_SYMBOL_ERR = 0
NOT_REACHED_FINAL_STATE = 1
REACHED_FINAL_STATE = 2


class NewState:
    state = ''
    stack = ''

    def __init__(self, cur_state, cur_stack):
        self.state = cur_state
        self.stack = cur_stack


class PDA:
    _states = []
    _inputs = []
    _pd_inputs = []
    _sigma = None
    _start_state = ''
    _start_pd_character = ''
    _final_states = []
    _progress = []

    def __init__(self, states: list, inputs: list, pd_inputs: list,
                 transitions: dict, start_state: str, start_pd_character: str, final_states: list):
        self._states = states
        self.total_states = len(states)

        self._inputs = inputs
        self._alphabet_characters = len(inputs)

        self._pd_inputs = pd_inputs
        self._pd_alphabet_characters = len(pd_inputs)

        self._sigma = transitions

        self._start_state = start_state

        self._start_pd_character = start_pd_character

        self._final_states = final_states
        self._total_final_states = len(final_states)

        self._progress.append(NewState(start_state, start_pd_character))

    def makeStep(self, current_symbol: chr) -> int:
        if current_symbol not in self._inputs and current_symbol != '':
            return UNKNOWN_SYMBOL_ERR

        new_step = []
        transitions = []
        empty_transitions = []

        for cur_state in self._progress:
            state = cur_state.state
            if len(cur_state.stack) == 0:
                top = ''
            else:
                top = cur_state.stack[0]

            cur_state.stack = cur_state.stack[1:]

            try:
                if (state, current_symbol, top) in self._sigma:
                    transitions = self._sigma[(state, current_symbol, top)]
                    for temp in transitions:
                        print('δ(' + str(cur_state.state) +
                              str(', ' + current_symbol + ', ').replace(', ,', ', λ,') +
                              top + str(cur_state.stack) + ') -> (' + str(temp[0]) +
                              str(', ' + str(temp[1]) + str(cur_state.stack) + ')').replace(', )', ', λ)'))

                # if (state, '', top) in self._sigma:
                #     empty_transitions = self._sigma[(state, '', top)]
                #     for temp in empty_transitions:
                #         print('δ(' + str(cur_state.state) + ', ' + 'e' + ', ' + top + str(cur_state.stack) +
                #               ') -> (' + str(temp[0]) + ', ' + str(temp[1]) + str(cur_state.stack) + ')')

                for transition in transitions:
                    # δ(state, input, pop_stack) -> (new_state, push_stack)
                    # tuple( , ); transition(state, stack); transition(0, 1)
                    new_step.append(NewState(transition[0], transition[1] + cur_state.stack))

                # for transition in empty_transitions:
                #     new_step.append(NewState(transition[0], transition[1] + cur_state.stack))
            except Exception as e:
                # Чтобы IDE не ругалась
                print(e)

        print()

        self._progress = new_step

        for variable in self._progress:
            if (variable.state in self._final_states and
                    (variable.stack == '' or variable.stack == self._start_pd_character)):
                return REACHED_FINAL_STATE

        return NOT_REACHED_FINAL_STATE

    def is_done(self):
        for res in self._progress:
            if (len(res.stack) == 0 or res.stack == self._start_pd_character) and res.state in self._final_states:
                return False
            else:
                return True


if __name__ == "__main__":
    result = NOT_REACHED_FINAL_STATE

    # PDA description
    cur_pda = PDA(states=['q0', 'q1', 'q2'],
                  inputs=['a', 'b', 'c'],
                  pd_inputs=['a', 'b', 'c', 'Z'],

                  # δ(q, a, X) -> (p, γ)
                  # δ(state, input, pop_stack) -> (new_state, push_stack)
                  transitions={('q0', 'a', 'a'): [('q0', 'aa')],
                               ('q0', 'a', 'Z'): [('q0', 'aZ')],
                               ('q0', 'b', 'a'): [('q0', 'ba')],
                               ('q0', 'b', 'b'): [('q0', 'bb')],
                               ('q0', 'b', 'Z'): [('q0', 'bZ')],
                               ('q0', 'c', 'b'): [('q0', ''), ('q0', 'bc')],
                               ('q0', 'c', 'c'): [('q0', 'cc')],
                               ('q0', '', 'Z'): [('q1', 'ZZ')],
                               ('q0', '', 'a'): [('q1', '')],
                               ('q1', '', 'a'): [('q1', '')],
                               ('q1', '', 'Z'): [('q2', '')],
                               },
                  start_state='q0',
                  start_pd_character='Z',
                  final_states=['q2']
                  )

    print("Enter a string with 'a's, 'b's and 'c's:\nPress Enter Key to stop\n")

    input_str = input()
    i = 0

    while cur_pda.is_done():
        if i < len(input_str):
            symbol = input_str[i]
        else:
            symbol = ''
        i += 1

        result = cur_pda.makeStep(symbol)

        if UNKNOWN_SYMBOL_ERR == result:
            print('Unknown symbol error')
            break

    if REACHED_FINAL_STATE == result:
        print('Accepted')

    if NOT_REACHED_FINAL_STATE == result:
        print('Rejected')
