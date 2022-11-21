class Solution:
    def interpret(self, command: str) -> str:
        # com = {'G': 'G', '()': 'o', '(al)': 'al'}
        output = ''
        i = 0
        while i < len(command):
            # print(command[i])
            # print(command[i: i + 2])
            # print(command[i: i + 4])
            if command[i] == 'G':
                output += 'G'
                i += 1
            elif command[i: i + 2] == '()':
                output += 'o'
                i += 2
            elif command[i: i + 4] == '(al)':
                output += 'al'
                i += 4
        return output