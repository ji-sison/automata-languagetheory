
"""
CS 141 Python Module for Deterministic Finite Automata (DFA)
"""

class DFA():
    """
    Deterministic Finite Automata

    Attributes
    ---------
        states: set
            collection of states
        alphabet: set
            collection of symbols
        transition: dict
            transition function of the form transition[state][symbol]-> state
        start_state: str
            starting or initial state
        accept_states: set
            set of accepting or final states
        
    """

    def __init__(self, states = set(), alphabet = set(), transition = dict(), start_state = None, accept_states = set()):
        """
        Class initialization
        """
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transition = transition
        self.start_state = start_state
        self.accept_states = set(accept_states)

    def __repr__(self):
        """
        Class representation
        """
        return "Deterministic Finite Automata (DFA) at " +f"{hex(id(self))}"

    def __str__(self):
        """
        Class string representation
        """
        str_self = (
            self.__repr__() + "\n"
            + "States: " + f"{self.states}\n"
            + "Symbols: " + f"{self.alphabet}\n"
            + "Start States: " + f"{self.start_state}\n"
            + "Accept: " + f"{self.accept_states}\n"
            + self.str_transition()
            )
        return str_self

    def str_transition(self):
        """
        String representation of the transition function
        """

        string = " Transitions: state, symbol -> state"
        for state in self.transition:
            state_transitions = self.transition[state]
            for symbol in self.alphabet:
                string += "\n\t" + state + ", " + symbol + " -> " + state_transitions[symbol]
        return string

    def accepts(self, input_string = ""):
        """
        Returns True if DFA accept the input string (default is the empty string) otherwise False

        """
        current_state = self.start_state
        for idx in range(len(input_string)):
            symbol = input_string[idx]
            current_state = self.transition[current_state][symbol]
        if current_state in self.accept_states:
            return True
        else:
            return False

            # graphvis