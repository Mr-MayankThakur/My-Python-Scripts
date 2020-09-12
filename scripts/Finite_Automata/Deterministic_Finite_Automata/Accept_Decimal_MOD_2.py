# -*- coding: utf-8 -*-
"""
DFA machine which accepts Decimal numbers divisible by 2
ie. over the input alphabets {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}.

Requirements:
    -> Python 3.0 or higher

Usage:
    -> Simply run this script with python and follow on screen instructions.
"""
__script_name__ = "DFA accepting Decimal Numbers Divisible by 2"
__version__ = "1.0.0"
__author__ = "Mayank Thakur"
__date__ = "12-09-2020"


class CustomDFAState:
    """
    This class's sole purpose is to abstract away the repeating conditional transition statements in all states.

    Note:
        This class supports defining any number of transitions but you have to define them individually for each state,
         for a generalized way of defining unlimited number of alphabet and states
         refer: https://github.com/Mr-MayankThakur/My-Python-Scripts/blob/master/scripts/Deterministic_Finite_Automata/Generalized_DFA.py
    """

    def __init__(self, state_name, final=False):
        """
        Custom DFA State Constructor

        Args:
            state_name: str
            final: bool, defines if this state should be considered as final or not.
        """

        self.name = state_name
        self.is_final = final

        # pre-initializing the transitions for both inputs as self loops
        self.transition_dict = dict()

    def define_transition(self, transition_dictionary):
        """
        Function to define transitions

        Define any number of transitions in this function as transition_dictionary in
        form of python dict :
            {<input_value> = <state_to_transition>}

        Args:
            transition_dictionary: dict
                python dict where keys are string and values are CustomDFAState instance.

        Returns: None

        Examples:
            define_transition({'0':state_1, '2':state_3})

        """
        self.transition_dict = transition_dictionary

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

        current_input = input_string[0]

        # call the next appropriate state with remaining input
        try:
            return self.transition_dict[current_input].run(input_string[1:])
        except KeyError:
            raise (KeyError("Invalid String Entered: {}".format(input_string[0])))


if __name__ == "__main__":
    print("pre-initializing states")

    state_0 = CustomDFAState(state_name='q0', final=True)
    state_1 = CustomDFAState(state_name='q1')

    # defining transitions for all the states
    state_0.define_transition({
        '0': state_0,
        '2': state_0,
        '4': state_0,
        '6': state_0,
        '8': state_0,
        '1': state_1,
        '3': state_1,
        '5': state_1,
        '7': state_1,
        '9': state_1,
    })
    state_1.define_transition({
        '0': state_0,
        '2': state_0,
        '4': state_0,
        '6': state_0,
        '8': state_0,
        '1': state_1,
        '3': state_1,
        '5': state_1,
        '7': state_1,
        '9': state_1,
    })
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
