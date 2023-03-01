from dfa import DFA

if __name__ == "__main__":
    M = DFA(states = {"q1", "q2", "q3"}, alphabet = {"0", "1"}, 
            transition = {
                "q1": {"0": "q1", "1": "q2"},
                "q2": {"0": "q3", "1": "q2"},
                "q3": {"0": "q2", "1": "q2"},
                },
            start_state = "q1", accept_states = {"q2"})
    print(M)
    for input_string in ["100", "101", "111"]:
        print(M.__repr__() + " accepts" + input_string + "? " + str(M.accepts(input_string)))
