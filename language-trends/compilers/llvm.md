# LLVM

[Fireship](https://www.youtube.com/watch?v=BT2Cv-Tjq7Q)

## What is LLVM?

Want to build your own programming language? LLVM is a tool for building and optimizing compilers and forms the backbone of many languages like Rust, Swift, CUDA, C, and C++.

LLVM represents source code in a language agnostic code called `intermediate representation (IR)`.

## What is the compiler made out of?

A compiler can be broken down into three parts:

1. The `frontend` parses source code text and converts it into IR
2. The `middle-end` analyzes and optimizes IR
3. The `backend` converts IR into native machine code

### How does the compiler's frontend parse source code?

1. A `lexer` turns raw text into tokens (literals, identifiers, keywords, separators, and operators)
2. An `abstract syntax tree (AST)` represents the code structure and how different tokens relate to each other. Each token node is given its own class
3. A `parser` loops over each token to construct the AST
