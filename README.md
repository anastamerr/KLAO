# German Number Simplifier

A Python utility that simplifies and explains numbers in German text, making them more readable and relatable.

## Overview

This project provides a Python function that takes German text containing numbers and transforms them into more understandable formats by:
- Rounding large numbers
- Converting percentages to descriptive text
- Adding contextual explanations
- Using figurative comparisons
- Preserving special cases like dates and measurements

## Project Versions

This project is available in two versions:

1. **Simple Version** (`klao/simplifier.py`):
   - Single file implementation
   - Easy to use and understand
   - Perfect for quick use or learning
   - Just copy and run

2. **Organized Version** (`klao/src/*`):
   - Full project structure
   - Modular design
   - Better for larger applications
   - Includes interactive interface

## Quick Start (Simple Version)

1. Copy `simplifier.py` and run directly:
```bash
python simplifier.py
```

This will run all test cases and show results immediately.

```python
# Simple usage in your code
from simplifier import simplify_numbers

text = "324.620,22 Euro wurden gespendet."
result = simplify_numbers(text)
print(result)  # "etwa 325.000 Euro wurden gespendet."
```

## Full Version Structure

```
klao/
├── src/
│   ├── number_simplifier/
│   │   ├── number_simplifier.py    # Main simplifier class
│   │   ├── patterns.py      # Regular expression patterns
│   │   └── constants.py     # Mappings and constants
│   └── utils/
│       └── text_utils.py    # Helper functions
├── tests/
│   └── test_simplifier.py   # Test cases
├── main.py                  # Interactive runner
├── simplifier.py            # Simple version and Direct implementation
└── README.md
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/anastamerr/KLAO.git
   cd KLAO
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Unix or MacOS:
   source .venv/bin/activate
   ```

## Running the Application

Three ways to use this application:

1. **Simple Direct Mode**:
   ```bash
   python simplifier.py
   ```
   This runs all test cases directly and shows input/output pairs in a simple format.

2. **Interactive Mode** (Full Version):
   ```bash
   python main.py
   ```
   This provides a menu with options to:
   - Run all test cases
   - Enter your own text interactively
   - Exit the program

3. **Module Import** (Both Versions):
   ```python
   # Simple version
   from simplifier import simplify_numbers
   
   # OR Full version
   from src.number_simplifier.simplifier import NumberSimplifier
   ```

## Example Transformations

```python
# Monetary values
"1.000.000 Euro wurden gespendet."
→ "etwa 1,0 Million Euro (So viel Geld, dass man 100 Autos kaufen könnte) wurden gespendet."

# People counts
"10.000 Menschen waren anwesend."
→ "etwa 10.000 Menschen (So viele Menschen, wie in ein großes Fußballstadion passen) waren anwesend."

# Percentages
"30 Prozent der Fläche sind betroffen."
→ "Ein Drittel, also ein Stück von drei gleich großen Teilen sind betroffen."

# Weights
"250 Kilogramm wiegt die Lieferung."
→ "etwa 250 Kilogramm (So schwer wie ein großer Kühlschrank) wiegt die Lieferung."
```

## Features

1. **Number Rounding**
   - Simplifies large numbers: `324.620,22 Euro → etwa 325.000 Euro`
   - Handles decimal numbers: `38,7 → etwa 39`

2. **Percentage Translations**
   - Common percentages to words: `25 Prozent → jeder Vierte`
   - Descriptive phrases: `90 Prozent → fast alle`

3. **Special Case Handling**
   - Preserves dates: `Am 1. Januar 2024`
   - Maintains pH values: `pH-Wert beträgt 7,4`
   - Handles time formats: `15:30 Uhr`

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Anas Osman

## Contact

For any questions or suggestions, please open an issue on GitHub or contact via:
- GitHub: [@anastamerr](https://github.com/anastamerr)