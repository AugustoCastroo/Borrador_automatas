import re

class NFA:
    def __init__(self):
        # Definimos las transiciones del AFND usando expresiones regulares
        self.transitions = {
            0: {'є': [3, 0], 'a': [1], 'b': [2]},
            1: {'є': [3]},
            2: {'є': [3]},
            3: {'є': [0, 4]},
            4: {'a': [5], 'b': [6], 'є': [7]},
            5: {'є': [8]},
            6: {'є': [8]},
            7: {'є': [8]},
            8: {}
        }
        # Establecemos los estados de aceptación
        self.accepting_states = {3, 4, 6, 8}
        # Inicializamos los estados actuales (comenzamos con el estado inicial)
        self.current_states = {0}

    def process_input(self, input_string):
        for symbol in input_string:
            self._process_symbol(symbol)
        return any(state in self.accepting_states for state in self.current_states)

    def _process_symbol(self, symbol):
        next_states = set()
        for state in self.current_states:
            for regex, target_states in self.transitions[state].items():
                if re.match(regex, symbol):
                    next_states |= set(target_states)
        self.current_states = next_states

if __name__ == "__main__":
    nfa = NFA()
    input_string = input("Ingresa una cadena de entrada (con 'a' y 'b'): ")
    print("Estado\tCaracter\tSiguiente Estado")
    for symbol in input_string:
        nfa._process_symbol(symbol)
        current_state = ", ".join(map(str, nfa.current_states))
        next_states = ", ".join(map(str, nfa.transitions[state][symbol]) for state in nfa.current_states if symbol in nfa.transitions[state])
        print(f"{current_state}\t{symbol}\t\t{next_states}")
    if nfa.process_input(input_string):
        print(f"\nLa cadena '{input_string}' es aceptada por el AFND.")
    else:
        print(f"\nLa cadena '{input_string}' no es aceptada por el AFND.")