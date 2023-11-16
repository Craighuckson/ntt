from HackAssembler import sanitize_file, make_stack, Code, Parser


def test_sanitize_file():
    assert sanitize_file([]) == []
    assert sanitize_file(['MOV A, B', 'ADD A, C', 'SUB B, D']) == ['MOV A, B', 'ADD A, C', 'SUB B, D']
    assert sanitize_file(['// This is a comment', '// Another comment', '// Comment']) == []
    assert sanitize_file(['   ', ' ', '\t', '\n']) == []
    assert sanitize_file(['MOV A, B // Move B to A', ' ADD A, C ', ' SUB B, D // Subtract D from B ']) == ['MOV A, B', 'ADD A, C', 'SUB B, D']


def test_make_stack():
    assert make_stack([]) == []
    assert make_stack(['MOV A, B', 'ADD A, C', 'SUB B, D']) == ['SUB B, D', 'ADD A, C', 'MOV A, B']
    assert make_stack(['1', '2', '3', '4', '5']) == ['5', '4', '3', '2', '1']


def test_dest():
    dest = Code.dest
    assert dest("M") == "001"
    assert dest("D") == "010"
    assert dest("MD") == "011"
    assert dest("A") == "100"
    assert dest("AM") == "101"
    assert dest("AD") == "110"
    assert dest("AMD") == "111"
    assert dest("XYZ") == "000"  # Test with an invalid mnemonic


def test_parser_dest():
    # mock a fake file to test with

    p = Parser("C:\\Users\\Cr\\ntt\\projects\\06\\Add.asm")
    p.instruction_type = "C_COMMAND"
    assert p.dest("D=M") == "D"
    assert p.dest("M=D") == "M"
    assert p.dest("D;JGT") == None


def test_get_instruction_type():
    p = Parser("C:\\Users\\Cr\\ntt\\projects\\06\\Add.asm")
    assert p.get_instruction_type("@2") == "A_COMMAND"
    assert p.get_instruction_type("(LOOP)") == "L_COMMAND"
    assert p.get_instruction_type("D=D+A") == "C_COMMAND"
