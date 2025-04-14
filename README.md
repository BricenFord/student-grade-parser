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

## How to Format `input.txt`

Each student record should contain the following fields, in order:

1. **9-digit ID number**  
2. **First name**  
3. **Last name**  
4. **Final score** (0–100)  
5. **E or L** (Eager or Lazy — participation level)  
6. *(Optional)* City and/or state (can be 0, 1, or 2 words)

### Notes:
- Records can be on the same line or span multiple lines
- Whitespace doesn't matter — the program handles line breaks
- There must be at least 7 students for correct ranking