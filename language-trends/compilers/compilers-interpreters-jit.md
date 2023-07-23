# AOT Compilers, JIT Compilers, and Interpreters

[Bits and Bytes](https://www.youtube.com/watch?v=_C5AHaS1mOA)

[Engineer Man](https://www.youtube.com/watch?v=5rn_MAspYFM)

## Ahead-of-Time Compilers

`AOT compilation` takes place prior to runtime and produces a native executable.

Languages that are usually implemented with AOT compilation:

> C, C++, Rust, Go

## Just-in-Time Compilers

`JIT compilation` is an interpreter feature that might take place during runtime; source code is converted on the fly to native machine code.

Language implementations usually need interpreters with JIT compilation when the language has dynamic and loose typing. For example, this Python code cannot be AOT compiled because we do not know the size of `name` until runtime:

```
# python3
name = input('what is your name?')
```

## Interpreters

An pure interpreter is a program that reads and executes code without compiling to native machine code. However, this is very slow, so interpreters with JIT compilation are used more often.

Language implementations that used to only use pure interpretation:

> JavaScript, Ruby, PHP

## Intermediate representation

Some language implementations might use a compiler to output an `intermediate language` designed to be interpreted. Bytecode interpreters 

Language implementations that utilize intermediate representation:

> Java, C#, C++ (.NET), Python (CPython)
