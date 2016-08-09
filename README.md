# regex
A regex parser using FSM(Finite State Machine)

## project structure
**_Scanner.py_**: Convert regular expression into tokens stream

**_Parser.py_**: Parse tokens stream, generate a abstract syntax tree for 
specific regex

**_NFA.py_**: A non-deterministic automaton implementation including three
 basic operations: 
 * `|`(`or` operator): alternative operation
 * `&`(`and` operator): concatenating operation
 * `~`(`invert` operator): repeating operation

**_NFABuilder.py_**: A builder wrapper for nfa

**_test_**: a bunch of unittest files