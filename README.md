# Student Grade Parser

This Python project was developed for CS-3323 - Principles of Programming Languages. It reads a raw student data file (`input.txt`), processes each record, ranks the students based on their final scores and class participation, assigns letter grades accordingly, and outputs a clean, alphabetically sorted HTML table (`output.html`).

## Features

- Parses unstructured student data from `input.txt`
- Handles multiline and variable-length student records
- Ranks students by score and eagerness (E > L)
- Assigns letter grades using a ranked tier system:
  - Top ⌊n/3⌋ → Grade A
  - Next ⌊n/3⌋ → Grade B
  - Bottom ⌈n/10⌉ → Grade F
  - Remaining students: Grade C (if Eager), D (if Lazy)
- Outputs a neatly formatted HTML table sorted by:
  - Last name → First name → ID