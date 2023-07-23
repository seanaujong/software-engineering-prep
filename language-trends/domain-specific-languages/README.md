# Domain Specific Languages

[StackOverflow](https://stackoverflow.com/questions/809574/what-is-a-domain-specific-language-anybody-using-it-and-in-what-way)

> A domain specific language is a language that's written to deal with a specific domain or set of concerns. There are a lot of them around, like make, ant, and rake for describing software builds, or lexx and yacc for language construction.

You can think of DSLs as complex arguments for functions written in a more general programming language. The real programming language parses the DSL code and does something with it, typically, the DSL code only focuses on the what you want to do, and the larger system figures out the how.

Examples of DSL include all query languages (SQL, XPath, ...), all template languages (Django, Smarty, ...), shell scripts, especially including stuff like twill, a command driven web browser (mostly used for automated test), data storage and exchange languages (XML, YAML, ...), and document languages like LaTex, HTML or CSS.

Some languages with very flexible syntax like TCL and Lisp build their DSL directly into the language... when possible. The majority of languages use strings, usually loaded from external files.

Are there any particular advantages of using them? Using them for their intended purposes is very advantageous to the point you will turn to them without knowing, just like you have been using (I presume) SQL or HTML without thinking of them as DSLs.

I'll dare saying there are enough DSLs out there for any sort of application you may need; you almost certainly don't need to learn how to write your own one.
