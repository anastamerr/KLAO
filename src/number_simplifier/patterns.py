
# Basic patterns
NUMBER_PATTERN = r'-?\d+(?:\.\d+)*(?:,\d+)?'
CURRENCY_PATTERN = rf'{NUMBER_PATTERN}\s*(?:€|Euro)'
PERCENTAGE_PATTERN = rf'(\d+(?:,\d+)?)\s*Prozent'

# Ignore patterns
IGNORE_PATTERNS = [
    r'\d{1,2}\.\s+(?:Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)',
    r'\d{4}(?=\s+(?:waren|gab))',  # Year patterns
    r'\b\d{2}:\d{2}\b',  # Time patterns
    r'\bpH-Wert\s+\d+[.,]\d+\b'  # pH values
]

# Context patterns
MENSCHEN_PATTERN = r'(\d+(?:\.\d+)*(?:,\d+)?)\s*(Menschen|Teilnehmer)'