# -*- coding: utf-8 -*-
"""
Non Deterministic Finite Automata to Deterministic Finite Automata converter.

Requirements:
    -> Python 3.0 or higher

Usage:
    -> Simply run this script with python and follow on screen instructions.
"""
__script_name__ = "NDFA to DFA Converter"
__version__ = "1.0.0"
__author__ = "Mayank Thakur"
__date__ = "24-09-2020"

"""
General Structure of input of transition table:
    {
        <state_name>:{
                input_alphabet1: {transition state}
                input_alphabet1: {transition state}
            }
        <state_name>:{
                input_alphabet1: {transition state}
                input_alphabet1: {transition state}
            }
    }

Note:
    state name should not have space in it
    write space seperated transition states if there are more than 1
    in case of no transition use empty set
"""


def generate_state_output(transition_dict: dict, new_state: frozenset, input_alphabet: str):
    """
    This function generates the output of a new or existing state by taking union of
    the output of all the states in new_state for the input_alphabet
    Args:
        transition_dict: dict
                the original transition dictionary of NDFA
        new_state: frozenset
                new state in the form of set containing states from which it is generated
        input_alphabet: str
                input alphabet for which the output is needed

    Returns: set
        output state for the corresponding new state.
    """
    output = frozenset()
    for state in new_state:

        # skip if the state is empty
        if state == '':
            continue

        # convert state to hashable set
        hashable_state = frozenset({state})
        output = output.union(transition_dict[hashable_state][input_alphabet])

    return output - {''}


def generate_dfa_transition_dict(nfa_transition_dict: dict, start_state: str, input_alphabets: set, final_states: set):
    """
    This function generates DFA from given NFA transition dictionary
    """

    # initial empty variables
    dfa_states = set()
    dfa_transition_dict = dict()
    unprocessed_states = set(frozenset({start_state}))  # set of states which are yet to be processed

    # while loop which runs un-till we don't have any state whose transitions are not calculated yet
    while len(unprocessed_states) != 0:
        current_state = unprocessed_states.pop()
        current_transition_definition = dict()

        dfa_states.add(current_state)

        for alphabet in input_alphabets:
            output_state = generate_state_output(nfa_transition_dict, current_state, alphabet)

            if (output_state != frozenset({''})) and (output_state not in dfa_states):
                unprocessed_states.add(output_state)

            current_transition_definition[alphabet] = output_state

        dfa_transition_dict[current_state] = current_transition_definition

    # defining dfa final states
    dfa_final_states = set()

    for state in dfa_states:
        for f_state in final_states:
            if len(state.intersection(f_state)) > 0:
                dfa_final_states.add(state)
            break

    return dfa_transition_dict, dfa_states, dfa_final_states


def print_transition_dict(transition_dict: dict, alphabets: set):
    """
    this function takes a transition dict and prints it in tabular form.
    """

    # getting length of longest state name
    max_state_length = 0
    for input_sets in transition_dict.values():
        for state_name in input_sets.values():
            max_state_length = max(len(str(list(state_name))), max_state_length)

    # adding extra padding to max state length
    max_state_length += 4

    # printing alphabets as header
    print(" " * max_state_length, end="|")
    for alphabet in sorted(alphabets):
        print(f"{alphabet:^{max_state_length}}", end="|")
    print("")

    print("-" * max_state_length * (len(alphabets) + 2))

    for state, input_dict in transition_dict.items():
        print(f"{str(list(state)):^{max_state_length}}", end="|")

        for input_alphabet, input_state in sorted(input_dict.items(), key=lambda x: x[0]):
            print(f"{str(list(input_state)):^{max_state_length}}", end="|")

        print("")


def input_transition_dict():
    """
    This function takes the user input for generating a systematic NFA transition python dictionary.
    """

    alphabets = set(input("Please enter space separated alphabet list: ").split(" "))

    states = set(input("Please enter space separated states list: ").split(" "))

    start_state = frozenset({input("Please enter name of start state[it should be single state name]: ")})

    final_states = set(map(lambda x: frozenset({x}), input("Please enter space separated list of final states: ").split(" ")))

    transition_dict = dict()

    print("\nPlease enter corresponding state outputs as space separated list")
    print("***In case of no transition do not enter anything and just press enter***\n")

    for state in states:
        sub_state_dict = dict()
        for alphabet in alphabets:
            transition_states = input(f"transition state(s) from {state} for {alphabet}: ").split(" ")
            sub_state_dict[alphabet] = frozenset(transition_states)
        transition_dict[frozenset({state})] = sub_state_dict

    return transition_dict, alphabets, final_states, start_state


if __name__ == "__main__":

    while True:
        transition_dict, alphabets, final_states, start_state = input_transition_dict()

        print("\nInput NFA transition state table: ")
        print_transition_dict(transition_dict, alphabets)

        print(f"start state: {start_state}")
        print(f"final_state: {final_states}")

        print("\nPlease check that the above transition table satisfies your input: ")
        print("To continue enter y (Default)")
        print("To re-enter press n")

        user_confirmation = input("Input:  ")

        if user_confirmation.lower() != 'n':
            break

    print("Please wait conversion in progress...")

    dfa_transition, dfa_states, dfa_final_states = generate_dfa_transition_dict(transition_dict, start_state, alphabets, final_states)

    print("\nOutputs:")

    print_transition_dict(dfa_transition, alphabets)
    print()
    print(f"DFA_states: {dfa_states}")
    print(f"final_DFA_states = {dfa_final_states}")
