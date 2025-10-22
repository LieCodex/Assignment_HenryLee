# states = {'A', 'B', 'C'}


# # print 'a' whenever the sequence '01' is encountered


class Assignmet():
    def dfa(self, value):
        state = 0
        for char in value:
            if state == 0:
                if char == '0':
                    state = 1
                    print('b')
                elif char == '1':
                    state = 0
                    print('b')
                else:
                    print("Invalid input")
                    return
            elif state == 1:
                if char == '0':
                    state = 1
                    print('b')
                elif char == '1':
                    state = 2
                    print('a')
                else:
                    print("Invalid input")
                    return
            elif state == 2:
                if char == '0':
                    state = 1
                    print('b')
                elif char == '1':
                    state = 0
                    print('b')
                else:
                    print("Invalid input")

if __name__ == "__main__":
    assignmet = Assignmet()
    assignmet.dfa(input("Enter a string of 1s and 0s: "))