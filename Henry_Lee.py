# states = {'A', 'B', 'C'}
# let state A be 0, B be 1, C be 2

# # print 'a' whenever the sequence '01' is encountered


class Assignmet():
    
    def Mealy(self, value):
        state = 0
        states = [state]
        outputs = []
        for char in value:
            if char not in '01':
                print("Invalid input")
                return
            if state == 0:
                if char == '0':
                    state = 1
                    outputs.append('b')
                elif char == '1':
                    state = 0
                    outputs.append('b')
            elif state == 1:
                if char == '0':
                    state = 1
                    outputs.append('b')
                elif char == '1':
                    state = 2
                    outputs.append('a')
            elif state == 2:
                if char == '0':
                    state = 1
                    outputs.append('b')
                elif char == '1':
                    state = 0
                    outputs.append('b')
            states.append(state)
        print("States:", '->'.join(map(str, states)))
        print("Outputs:", ''.join(outputs))

    def moore(self, value):
        state = 0
        states = [state]
        outputs = []
        # initial output for state 0
        outputs.append('b')
        for char in value:
            if char not in '01':
                print("Invalid input")
                return
            if state == 0:
                if char == '0':
                    state = 1
                elif char == '1':
                    state = 0
            elif state == 1:
                if char == '0':
                    state = 1
                elif char == '1':
                    state = 2
            elif state == 2:
                if char == '0':
                    state = 1
                elif char == '1':
                    state = 0
            states.append(state)
            # current Moore implementation outputs 'b' for all states
            outputs.append('b')
        print("States:", '->'.join(map(str, states)))
        print("Outputs:", ''.join(outputs))

if __name__ == "__main__":
    assignmet1 = Assignmet()
    assignmet1.Mealy(input("Enter a string of 1s and 0s: "))
    assignmet1.moore(input("Enter a string of 1s and 0s: "))