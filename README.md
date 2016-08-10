# Introduction
A regex parser using FSM(Finite State Machine)

## Project Structure
**_Scanner.py_**: Convert regular expression into tokens stream

**_Parser.py_**: Parse tokens stream, generate a abstract syntax tree for 
specific regex

**_NFA.py_**: A non-deterministic automaton implementation including three
 basic operations: 
 * `|`(`or` operator): alternative operation
 * `&`(`and` operator): concatenating operation
 * `~`(`invert` operator): repeating operation

**_NFABuilder.py_**: A builder wrapper for nfa

**_tests_**: A bunch of unittest files

## Example
```python
if __name__ == '__main__':
    scanner = Scanner('(a|b)*abb')
    scanner.lex()

    parser = Parser(scanner.tokens)
    parser.parse()
    print(parser.ast)

    nfa = NFABuilder.ast_to_nfa(parser.ast)
    print(nfa)
```
_output_:
* abstract syntax tree:
```
Cat
	Cat
		Cat
			Star
				|
					a
					b
			a
		b
	b
```
* nfa:
```
size: 11 start: 0, final: 10, transactions:
 from 0 to 1 when input is EPS
from 0 to 7 when input is EPS
from 1 to 2 when input is EPS
from 1 to 4 when input is EPS
from 2 to 3 when input is a
from 3 to 6 when input is EPS
from 4 to 5 when input is b
from 5 to 6 when input is EPS
from 6 to 1 when input is EPS
from 6 to 7 when input is EPS
from 7 to 8 when input is a
from 8 to 9 when input is b
from 9 to 10 when input is b
```
