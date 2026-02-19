# PyTools

## Overview

PyTools provides a set of single-purpose command-line programs that share a common invocation model and output contract.
Each command performs one well-defined operation and favors explicit behavior over implicit defaults. Commands are
designed to be composable in shell pipelines and deterministic unless interacting with external state.

The project is intentionally **pedantic but practical**: behavior is specified precisely where it affects correct usage,
and kept simple where it does not.

------------------------------------------------------------------------

## Design Philosophy

PyTools follows a small set of operational rules:

- **Single responsibility** --- each program performs one operation on a text stream or structured input.
- **Pipeline first** --- all tools read from `stdin` when no input file is provided and write results to `stdout`.
- **Deterministic by default** --- identical input produces identical output unless the program explicitly depends on
  time, environment, or filesystem state.
- **Explicit side effects** --- programs that touch the filesystem or external state document that behavior.
- **TTY-aware formatting** --- ANSI rendering is applied only when output is a terminal; otherwise plain text is
  emitted.
- **Stable output contracts** --- output shape and ordering are defined and suitable for downstream processing.

These constraints make the tools predictable, scriptable, and safe for composition.

------------------------------------------------------------------------

## Installation

Python ≥ 3.12 is required.

Clone the repository and install required package dependencies:

``` bash
git clone <repo-url>
pip3 install colorama
pip3 install python-dateutil
pip3 install requests
```

------------------------------------------------------------------------

## Command Model

All PyTools commands follow the same execution model:

1. **Input resolution**
    - Read from `stdin` if no path is provided
    - Otherwise, read from the specified file(s)
2. **Normalization**
    - Input is converted to a canonical internal representation so downstream logic does not depend on superficial
      differences (line endings, trailing whitespace, etc.)
3. **Core operation**
    - A pure transformation whenever possible
4. **Output**
    - Written to `stdout`
    - Errors written to `stderr`
    - Non-zero exit codes only for user or system errors

Unless otherwise stated, tools are **stream-safe** and do not buffer the entire input unnecessarily.

------------------------------------------------------------------------

## Architecture

PyTools is layered to separate pure logic from side effects:

    Programs → CLI framework → Text/Pattern primitives → Rendering → I/O boundary

### CLI Framework

Provides:

- Program lifecycle
- Argument parsing
- Input routing
- Output discipline and exit codes

### Text and Pattern Layer

Pure, deterministic transformations used by multiple tools. These functions do not perform I/O.

### Rendering Layer

ANSI and formatting utilities. Rendering is applied only when writing to a TTY.

### I/O Boundary

All filesystem and terminal interaction is isolated here. This makes core logic testable and deterministic.

------------------------------------------------------------------------

## Output Conventions

- **stdout** --- primary program output
- **stderr** --- diagnostics and error messages
- **Exit codes**
    - `0` --- success
    - `>0` --- user error, invalid input, or system failure

Unless a tool explicitly documents ordering semantics, output preserves the input order.

------------------------------------------------------------------------

## Tools

Each tool performs one well-defined operation. Examples assume input from `stdin` unless a file is specified.

### `dupe`

A program that filters duplicate or unique lines from files.

### `glue`

A program that concatenates files and standard input to standard output.

### `num`

A program that numbers lines from files and prints them to standard output.

### `order`

A program that sorts files and prints them to standard output.

### `peek`

A program that prints the first part of files.

### `scan`

A program that prints lines matching patterns in files.

### `seek`

A program that searches for files in a directory hierarchy.

### `show`

A program that prints files to standard output.

### `slice`

A program that splits lines in files into fields.

### `subs`

A program that replaces matching text in files.

### `tally`

A program that counts lines, words, and characters in files.

### `track`

A program that prints the last part of files, optionally following new lines.

### `when`

A program that displays the current calendar, with optional date and time.

### `where`

A program that displays current IP-based location information.

> Each command documents its own flags and output shape via `--help`.

------------------------------------------------------------------------

## Error Handling Contract

- Invalid user input results in a non-zero exit code and a concise diagnostic on `stderr`.
- Internal errors are not silently suppressed.
- Partial output is not emitted after a fatal error unless explicitly documented.

------------------------------------------------------------------------

## Development Notes

The codebase targets modern Python and follows these principles:

- Clarity over cleverness
- Explicit semantic contracts
- Weakest correct type annotations for inputs
- Pure functions separated from I/O
- Structured docstrings describing guarantees, not implementation trivia

Contributions should preserve the single-responsibility design and the pipeline-safe execution model.

------------------------------------------------------------------------

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).

You may redistribute and/or modify this software under the terms of the GPL-3.0.
A copy of the license is included in the `LICENSE` file and is also available
at: https://www.gnu.org/licenses/gpl-3.0.en.html
