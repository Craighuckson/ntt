#HackAssembler.py

import sys
import os

class Parser:
    def __init__(self, file):

        # Opens the input file/stream and gets ready to parse it

        pass


    def has_more_lines(self) -> bool:

        # Are there more commands in the input?

        pass

    def advance(self):

        # Reads the next command from the input and makes it the current command. Should be called only if has_more_lines() is true. Initially there is no current command.

        pass

    def instruction_type(self) -> str:

        # Returns the type of the current command:
        # A_COMMAND for @Xxx where Xxx is either a symbol or a decimal number
        # C_COMMAND for dest=comp;jump
        # L_COMMAND (actually, pseudo-command) for (Xxx) where Xxx is a symbol.

        pass

    def symbol(self):
        pass

    def dest(self):
        pass

    def comp(self):
        pass

    def jump(self):
        pass




class Code:
    
    def dest(self, mnemonic: str) -> str:

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
        
    def comp(self, mnemonic: str) -> str:

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

    def jump(self, mnemonic: str) -> str:

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
    
        # Reads the file and returns the contents as a string
    
        with open(file_name, 'r') as f:
            return f.read()


def main():

    # Reads the name of the file to be assembled

    # Creates a Parser object to parse the input file

    # Creates a Code object to translate Hack assembly language mnemonics into binary codes

    # Creates a SymbolTable object to manage the symbol table

    # Assemble the input file

    # Writes the translated Hack machine language to the output file

    pass

