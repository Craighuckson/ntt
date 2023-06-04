// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

// Q: How to implement multiplication only using addition?
// A: Use the fact that multiplication is repeated addition.

// Q: How to implement repeated addition?
// A: Use the fact that repeated addition is repeated incrementation.

// Q: How to implement repeated incrementation?
// A: Use the fact that incrementation is adding 1.

// pseudocode:

// R2 = 0
// while (R1 > 0) {
//   R2 = R2 + R0
//   R1 = R1 - 1
// }

// assembly:

@R2
M=0

(LOOP)
@R1
D=M

@END
D;JEQ
//Q: what does the line above do?
//A: if R1 == 0, jump to END


@R0
D=M

@R2
M=M+D

@R1
M=M-1

@LOOP
0;JMP


(END)
@END
0;JMP

