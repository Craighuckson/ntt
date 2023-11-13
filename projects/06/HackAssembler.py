#HackAssembler.py

import sys
import os

class Parser:
    def __init__(self, file):
        # Opens the input file/stream and gets ready to parse it
        self.file = file
        instruction_list = self.file.readlines()
        instruction_list = sanitize_file(instruction_list)
        self.instruction_stack = make_stack(instruction_list)
        self.current_command = None

    def has_more_lines(self) -> bool:

        # Are there more commands in the input?
        return len(self.instruction_stack) > 0

    def advance(self):

        # Reads the next command from the input and makes it the current command. Should be called only if has_more_lines() is true. Initially there is no current command.

        self.current_command = self.instruction_stack.pop()

    def instruction_type(self) -> str:

        # Returns the type of the current command:
        # A_COMMAND for @Xxx where Xxx is either a symbol or a decimal number
        # C_COMMAND for dest=comp;jump
        # L_COMMAND (actually, pseudo-command) for (Xxx) where Xxx is a symbol.

        if self.current_command[0] == '@':
            return 'A_COMMAND'
        elif self.current_command[0] == '(':
            return 'L_COMMAND'
        else:
            return 'C_COMMAND'

    def symbol(self):
        pass

    def dest(self):
        # Returns the dest mnemonic in the current C-command (8 possibilities).
        # Should be called only when instruction_type() is C_COMMAND.

        if self.current_command == 'C_COMMAND':
            return Code.dest(self.current_command)

    def comp(self):
        if self.current_command == 'C_COMMAND':
            return Code.comp(self.current_command)

    def jump(self):
        if self.current_command == 'C_COMMAND':
            return Code.jump(self.current_command)


class Code:

    @staticmethod
    def dest(mnemonic: str) -> str:

        # Returns the binary code of the dest mnemonic

        if mnemonic == "M":
            return "001"
        elif mnemonic == "D":
            return "010"
        elif mnemonic == "MD":
            return "011"
        elif mnemonic == "A":
            return "100"
        elif mnemonic == "AM":
            return "101"
        elif mnemonic == "AD":
            return "110"
        elif mnemonic == "AMD":
            return "111"
        else:
            return "000"
    @staticmethod
    def comp(mnemonic: str) -> str:

        # Returns the binary code of the comp mnemonic

        if mnemonic == "0":
            return "0101010"
        elif mnemonic == "1":
            return "0111111"
        elif mnemonic == "-1":
            return "0111010"
        elif mnemonic == "D":
            return "0001100"
        elif mnemonic == "A":
            return "0110000"
        elif mnemonic == "!D":
            return "0001101"
        elif mnemonic == "!A":
            return "0110001"
        elif mnemonic == "-D":
            return "0001111"
        elif mnemonic == "-A":
            return "0110011"
        elif mnemonic == "D+1":
            return "0011111"
        elif mnemonic == "A+1":
            return "0110111"
        elif mnemonic == "D-1":
            return "0001110"
        elif mnemonic == "A-1":
            return "0110010"
        elif mnemonic == "D+A":
            return "0000010"
        elif mnemonic == "D-A":
            return "0010011"
        elif mnemonic == "A-D":
            return "0000111"
        elif mnemonic == "D&A":
            return "0000000"
        elif mnemonic == "D|A":
            return "0010101"
        elif mnemonic == "M":
            return "1110000"
        elif mnemonic == "!M":
            return "1110001"
        elif mnemonic == "-M":
            return "1110011"
        elif mnemonic == "M+1":
            return "1110111"
        elif mnemonic == "M-1":
            return "1110010"
        elif mnemonic == "D+M":
            return "1000010"
        elif mnemonic == "D-M":
            return "1010011"
        elif mnemonic == "M-D":
            return "1000111"
        elif mnemonic == "D&M":
            return "1000000"
        elif mnemonic == "D|M":
            return "1010101"
        else:
            return "0000000"

    @staticmethod
    def jump(mnemonic: str) -> str:

        # Returns the binary code of the jump mnemonic

        if mnemonic == "JGT":
            return "001"
        elif mnemonic == "JEQ":
            return "010"
        elif mnemonic == "JGE":
            return "011"
        elif mnemonic == "JLT":
            return "100"
        elif mnemonic == "JNE":
            return "101"
        elif mnemonic == "JLE":
            return "110"
        elif mnemonic == "JMP":
            return "111"
        else:
            return "000"


class SymbolTable:

    def __init__(self):
        self.table = {}

    def add_entry(self, symbol, address):

        # Adds the pair (symbol, address) to the table

        self.table[symbol] = address

    def contains(self, symbol):

        # Returns true if the symbol table contains the given symbol

        return symbol in self.table

    def get_address(self, symbol):

        # Returns the address associated with the symbol

        return self.table[symbol]


class Assembler:
    pass


def read_file(file_name: str) -> str:

    # Reads the file and returns the contents as a list of instructions
    with open(file_name, "r") as f:
        return f.readlines()

def sanitize_file(instructions: list) -> list:

    # Removes comments and whitespace from the instructions

    sanitized_instructions = []

    for instruction in instructions:
        instruction = instruction.split("//")[0]
        instruction = instruction.strip()
        if instruction != "":
            sanitized_instructions.append(instruction)

    return sanitized_instructions

def make_stack(instructions: list):

    # Creates a stack of instructions by reversing the list
    # This is done so that the first instruction is at the top of the stack
    # and can be popped off first
    # This is done to make the assembly process easier

    stack = []

    for instruction in instructions:
        stack.append(instruction)

    stack.reverse()

    return stack

def main():

    # Reads the name of the file to be assembled from command line arg

    if len(sys.argv) != 2:
        print("Usage: python HackAssembler.py [Prog.asm]")
        sys.exit(1)

    file_name = sys.argv[1]

    # Creates a Parser object to parse the input file

    # Creates a Code object to translate Hack assembly language mnemonics into binary codes

    # Creates a SymbolTable object to manage the symbol table

    # Assemble the input file

    # Writes the translated Hack machine language to the output file

    pass
