# Compiling Java

[r/learnjava](https://www.reddit.com/r/learnjava/comments/vgow91/in_actual_practice_what_does_it_mean_to_say_that/id5aeo3/)

The interpreted/compiled distinction doesn't hold very well in modern times.

## Native Code Languages

Native code languages use a `compiler` whose final output stage is native code, often an executable file.

> C, C++, Pascal, Rust

## Scripting Languages

Scripting languages use an `interpreter` that reads source code at runtime. However, most interpreters don't execute source code directly. Before runtime, many interpreters use `tokenization` and `compilation` to produce either an `intermediate language` OR native code to execute. There is usually no executable file produced.

> Python, JavaScript

## Portable Compiled Languages

Portable compiled languages use a compiler that outputs an intermediate language. These languages require a `runtime environment` on the target platform to execute the application. The intermediate languages might be directly executed; they can also be JIT-compiled by multiple compilers.

### Java

For example, the `Java` compiler generates `bytecode` from Java source code. This bytecode can then be run on any `Java Virtual Machine` installed on a machine. JVMs will convert the bytecode into operations that are specific/native to that platform (Windows, Linux, Mac, etc.).

The JVM:

- might use an interpreter to execute bytecode
- might JIT-compile bytecode to native machine code
    - might use multiple JIT compilers of varying degrees of optimization
- might choose to recompile code for optimization

Java tracks statistics during runtime to further optimize its native code compilation. Different data sets might cause Java to compile differently.

> In practice, most of the code you run in Java, for any long-running process, will be native-code produced by the fast C1 HotSpot Just In Time compiler, or native-code produced by the more aggressively optimising C2 JIT compiler. The interpreter will be used until C1 has compiled the code in question, or if code is de-optimised (to allow C2 to re-optimise it to respond to changing execution statistics).
