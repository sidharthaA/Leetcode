class Solution:
    def interpret(self, command: str) -> str:
        output = ''
        i = 0
        while i < len(command):
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