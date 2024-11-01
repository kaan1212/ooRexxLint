# ooRexxLint

ooRexxLint is a [lint](https://en.wikipedia.org/wiki/Lint_(software)) tool for ooRexx and classic Rexx, which is inspired by [Pylint](https://en.wikipedia.org/wiki/Pylint).

## Linter rules

* Source file shall start with non-whitespace.
* Source file shall end in a newline character.
* No redundant newline characters allowed.
* No trailing whitespace allowed.
* Only 4 spaces per indentation level allowed.

## Setup

* [Download](https://www.python.org/downloads/) and install Python 3.12, or newer
* Download ooRexxLint.py file

## Usage

```
python ooRexxLint.py myprogram.rex

python ooRexxLint.py mydirectory
```

## Supported file extensions

* .rex
* .rexx
* .cls
* .testGroup

## Roadmap

* Implement an abstract syntax tree (AST) for improved code analysis
* Migrate ooRexxLint from Python to ooRexx programming language
* Provide native executables of ooRexxLint for Linux, Windows, and macOS

## Support

If you find ooRexxLint helpful, please star and watch this GitHub repository. This helps me to know that there is interest in maintenance and further development of ooRexxLint.
