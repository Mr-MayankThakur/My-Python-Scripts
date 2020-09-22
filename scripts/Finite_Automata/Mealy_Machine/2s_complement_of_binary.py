# -*- coding: utf-8 -*-
"""
This Finite Autamata, Mealy machine generates 2's complement of the given
Binary Number while ignoring the carry operation.

Steps:
    1. reverse the string.
    2. return same input untill first 1 is detected.
    3. After detecting First 1 return complement of the remaining string.
    4. again reverse the output and present to the user

Requirements:
    -> Python 3.0 or higher

Usage:
    -> Simply run this script with python and follow on screen instructions.
"""
__script_name__ = "Mealy Machine for 2's Complement of Binary No."
__version__ = "1.0.0"
__author__ = "Mayank Thakur"
__date__ = "22-09-2020"


def complement_output(input_string):
    """
    This function outputs the complement of the input string for binary numbers.
    ie.
    1 -> 0
    0 -> 1

    Args:
        input_string: str

    Returns: str

    """
    current_input = input_string[0]

    if current_input == '1':
        output = '0'
    elif current_input == '0':
        output = '1'
    else:
        raise TypeError(f"Invalid input {current_input}")

    if len(input_string[1:]) == 0:
        return output
    else:
        return output + complement_output(input_string[1:])


class MealyMachineState:
    """
    This class's sole purpose is to abstract away the repeating conditional transition statements in all states.
    in Mealy Machine Each transition has a associated output which is returned whenever we reach that state.

    """

    def __init__(self, state_name, final=False):
        """
        Custom DFA State Constructor

        Args:
            state_name: str
            state_output: str
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
            {<input_value> = [<state_to_transition>, <transition_output>}

        Args:
            transition_dictionary: dict
                python dict where keys are string and values are CustomDFAState instance.

        Returns: None

        Examples:
            define_transition({'0':[state_1, 0], '2':[state_3, 1]})

        """
        self.transition_dict = transition_dictionary

    def run(self, input_string: str, current_output=''):
        """
        This is a recursive function which calls the next state's run function according to the input.

        In case the input is of length 0 then the function returns True if it is final state else False,
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
            return current_output, self.is_final

        current_input = input_string[0]

        # call the next appropriate state with remaining input
        try:
            next_state = self.transition_dict[current_input][0]
            transition_output = self.transition_dict[current_input][1]
            return next_state.run(input_string[1:], current_output+transition_output)
        except KeyError:
            raise (KeyError("Invalid String Entered: {}".format(input_string[0])))


if __name__ == "__main__":
    print("pre-initializing states")

    state_0 = MealyMachineState(state_name='q0')
    state_1 = MealyMachineState(state_name='q1')

    # defining transitions for all the states
    state_0.define_transition({
        '0': [state_0, '0'],
        '1': [state_1, '1'],
    })

    state_1.define_transition({
        '0': [state_1, '1'],
        '1': [state_1, '0']
    })

    print("State Initialization Done!!\n")
    print("Input q to quit...")

    while True:

        user_input_string = input("Please enter a input string: ")

        if user_input_string.lower() == 'q':
            print("Exiting... \nHave a Good Day!!")
            break

        reversed_input = user_input_string[::-1]

        try:
            output, accepted = state_0.run(reversed_input)
            reversed_output = output[::-1]
            print("Output: {}".format(reversed_output))

        except TypeError as e:
            print(e)

        print('')  # just to have a clear output
