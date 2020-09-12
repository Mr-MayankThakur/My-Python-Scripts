# -*- coding: utf-8 -*-
"""
Generates a DFA machine from the given state-transition matrix and other info

Requirements:
    -> Python 3.0 or higher

Usage:
    -> Simply run this script with python and follow on screen instructions.
"""
__script_name__ = "Deterministic Finite Automata Generator"
__version__ = "0.1.0"
__author__ = "Mayank Thakur"
__date__ = "15-08-2020"


class DFA:
    """
    Generalized DFA Generator, it can be used to generate any DFA possible if you have a proper transition table.

    processing complexity: O(n) for input of size n
    """

    def __init__(self, alphabets, states, state_transition_matrix, final_states, start_state):
        """
        Deterministic Finite Automata Generator class.

        Args:
            alphabets: str list
                list of alphabets accepted by the DFA in same order as of columns in state transition matrix.
            states: str list
                list of state names in same order as of the rows in state transition matrix.
            state_transition_matrix: 2D nested str list
                2D nested list where rows represent states and columns represent different alphabets in ascending order.
            final_states: str list
                list of states which will be termed as final or accepted.
            start_state: string
                name of the state which will be considered as input state.
        """
        self.alphabets = sorted(alphabets)
        self.states = states
        self.st_matrix = state_transition_matrix
        self.final_states = final_states
        self.start_state = start_state
        self.dictionary_matrix = dict()

        self._generate_dictionary_matrix()

    def _generate_dictionary_matrix(self):

        for state_index, state in enumerate(self.states):
            state_dict = dict()
            for alphabet, transition_state in zip(self.alphabets, self.st_matrix[state_index]):
                state_dict[alphabet] = transition_state
            self.dictionary_matrix[state] = state_dict

    def info(self):
        """
        Prints the complete info about the generated Deterministic Finite Automata
        """

        # Alphabets
        print(f"Alphabets [{len(self.alphabets)}]: {self.alphabets}\n")

        # States
        print(f"States [{len(self.states)}]: {self.states}\n")

        # State Transition Matrix
        max_length = max(map(lambda x: len(x), ['States\Alphabets'] + self.states))

        for alphabet in ['States\Alphabets'] + self.alphabets:
            print("{:^{}}".format(alphabet, max_length), end='')
        print()

        for r, row in enumerate(self.st_matrix):
            print("{:^{}}".format(self.states[r], max_length), end='')

            for c, col in enumerate(row):
                print("{:^{}}".format(col, max_length), end='')

            print()

        print('-' * (max_length * (len(self.alphabets) + 1)))

    def run(self, input_string):
        """
        Process the given input string through the DFA returning the final output
        Args:
            input_string: str
                    input string containing only the allowed language alphabets.

        Returns: current_state:str, traversal_path: str list
        """

        # checking if string is valid
        assert len(input_string) > 0, "Empty String Passed"
        assert (set(input_string).issubset(set(self.alphabets))), 'Invalid String Given'

        current_state = self.start_state
        traversal_path = []

        for value in input_string:
            intermediate_state = self.dictionary_matrix[current_state][value]
            traversal_path.append(intermediate_state)
            current_state = intermediate_state

        return current_state, traversal_path


if __name__ == '__main__':
    '''
    test_matrix = [['q0',	'q1'],
    ['q2',	'q1'],
    ['q2',	'q2']]
    '''

    beginning_with_11 = [
        ['q3', 'q1'],
        ['q3', 'q2'],
        ['q2', 'q2'],
        ['q3', 'q3']
    ]

    language = ['0', '1']

    states = ['q0', 'q1', 'q2', 'q3']

    sample_DFA = DFA(alphabets=language,
                     states=states,
                     state_transition_matrix=beginning_with_11,
                     final_states='q2',
                     start_state='q0')
    sample_DFA.info()

    while True:
        input_string = input('please enter input string or E to exit: ')

        if input_string.lower() == "e":
            print('Ending run')
            break

        result, _ = sample_DFA.run(input_string)

        if result in sample_DFA.final_states:
            print(f"accepted at {result}")
        else:
            print(f'Not Accepted  at {result}')
