# -*- coding: utf-8 -*-
"""
DFA machine which accepts binary numbered strings divisible by 3 ie. over the input alphabets {0, 1}.

Requirements:
    -> Python 3.0 or higher

Usage:
    -> Simply run this script with python and follow on screen instructions.
"""
__script_name__ = "DFA accepting Binary Numbers Divisible by 11 (3 in decimal)"
__version__ = "1.0.0"
__author__ = "Mayank Thakur"
__date__ = "12-09-2020"


class DFAState:
    """
    This class's sole purpose is to abstract away the repeating conditional transition statements in all states.

    Note:
        This class supports "only two input alphabets {0, 1}", for defining unlimited number of alphabet and states
         refer: https://github.com/Mr-MayankThakur/My-Python-Scripts/blob/master/scripts/Deterministic_Finite_Automata/Generalized_DFA.py
    """

    def __init__(self, state_name, final=False):
        """
        DFA State Constructor

        Args:
            state_name: str
            final: bool, defines if this state should be considered as final or not.
        """

        self.name = state_name
        self.is_final = final

        # pre-initializing the transitions for both inputs as self loops
        self.transition_zero = self
        self.transition_one = self

    def define_transition(self, zero, one):
        """
        Function to define transitions upon inputs zero and one

        Args:
            zero: DFAState instance
            one: DFAState instance

        Returns: None
        """
        self.transition_one = one
        self.transition_zero = zero

    def run(self, input_string: str):
        """
        This is a recursive function which calls the next state's run function according to the input.

        In case the input is of length 1 only then the function returns True if it is final state else False,
        which states if the input is accepted or not.

        Args:
            input_string: str, containing only 0 or 1.

        Returns: bool
            -> True: if the last input ends in Final state
            -> False: if the last input ends at Non Final state

        Raises: TypeError, if input string does not contain 0 or 1 as string
        """

        # check if this is last input of string
        if len(input_string) == 0:
            return self.is_final

        # call the next appropriate state with remaining input
        if input_string[0] == '0':
            return self.transition_zero.run(input_string[1:])
        elif input_string[0] == '1':
            return self.transition_one.run(input_string[1:])
        else:
            raise(TypeError("Invalid String Entered: {}".format(input_string[0])))


if __name__ == "__main__":
    print("pre-initializing states")

    state_0 = DFAState(state_name='q0', final=True)
    state_1 = DFAState(state_name='q1')
    state_2 = DFAState(state_name='q2')

    # defining transitions for all the states
    state_0.define_transition(zero=state_0, one=state_1)
    state_1.define_transition(zero=state_2, one=state_0)
    state_2.define_transition(zero=state_1, one=state_2)

    print("State Initialization Done!!\n")
    print("Input q to quit...")

    while True:

        user_input_string = input("Please enter a input string: ")

        if user_input_string.lower() == 'q':
            print("Exiting... \nHave a Good Day!!")
            break

        try:
            accepted = state_0.run(user_input_string)
            if accepted:
                print("Accepted!!")
            else:
                print("Not Accepted :(")
        except TypeError as e:
            print(e)

        print('')  # just to have a clear output



