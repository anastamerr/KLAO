
import re
from typing import Optional
from ..utils.text_utils import convert_german_number, format_number
from .constants import PERCENTAGE_MAPPINGS, CONTEXTUAL_EXPLANATIONS
from .patterns import (
    NUMBER_PATTERN, CURRENCY_PATTERN, PERCENTAGE_PATTERN,
    IGNORE_PATTERNS, MENSCHEN_PATTERN
)


class NumberSimplifier:
    """A class to simplify numbers in German text according to specified rules."""

    def should_ignore(self, text: str, pos: int) -> bool:
        """Check if number at position should be ignored."""
        context = text[max(0, pos - 20):min(len(text), pos + 20)]
        return any(re.search(pattern, context) for pattern in IGNORE_PATTERNS)

    def get_descriptive_percentage(self, number: str) -> str:
        """Convert percentage to descriptive text."""
        try:
            num = float(number)

            # Check exact mappings first
            if int(num) in PERCENTAGE_MAPPINGS:
                return PERCENTAGE_MAPPINGS[int(num)]

            # Then handle ranges
            if num >= 90:
                return "fast alle"
            elif num <= 15:
                return "wenige"

            return f"{number} Prozent"
        except ValueError:
            return f"{number} Prozent"

    def simplify_number(self, match: re.Match, raw_text: str) -> str:
        """Simplify numbers according to rules."""
        original = match.group()
        start_pos = match.start()

        if self.should_ignore(raw_text, start_pos):
            return original

        number_match = re.search(NUMBER_PATTERN, original)
        if not number_match:
            return original

        number_str = number_match.group()
        number = convert_german_number(number_str)
        is_negative = number_str.startswith('-')

        try:
            num = float(number)
            abs_num = abs(num)

            # Handle currency with context
            if 'Euro' in original or '€' in original:
                if abs_num >= 1000000:
                    rounded = round(abs_num / 1000000, 1)
                    formatted_number = format_number(rounded)
                    sign = "etwa -" if is_negative else "etwa "
                    return f"{sign}{formatted_number} Million Euro ({CONTEXTUAL_EXPLANATIONS['million_euro']})"
                elif abs_num >= 1000:
                    rounded = round(abs_num, -3)
                    sign = "etwa -" if is_negative else "etwa "
                    return f"{sign}{int(rounded):,}".replace(',', '.') + " Euro"

            # Handle people with context
            menschen_match = re.search(MENSCHEN_PATTERN, original)
            if abs_num >= 10000 and menschen_match:
                rounded = round(abs_num, -3)
                sign = "etwa -" if is_negative else "etwa "
                unit = menschen_match.group(2)
                return f"{sign}{int(rounded):,}".replace(',', '.') + f" {unit} ({CONTEXTUAL_EXPLANATIONS['stadium']})"

            # Handle weights with context
            if 'Kilogramm' in original or 'kg' in original:
                if abs_num == 250:
                    sign = "etwa -" if is_negative else "etwa "
                    return f"{sign}{int(abs_num)} Kilogramm ({CONTEXTUAL_EXPLANATIONS['refrigerator']})"

            # Handle regular numbers over 1000
            if abs_num >= 1000:
                rounded = round(abs_num, -3)
                sign = "etwa -" if is_negative else "etwa "
                return f"{sign}{int(rounded):,}".replace(',', '.')

            # Handle decimal numbers
            elif '.' in str(abs_num):
                rounded = round(abs_num)
                sign = "etwa -" if is_negative else "etwa "
                return f"{sign}{abs(rounded)}"

            return original

        except ValueError:
            return original

    def simplify_numbers(self, raw_text: str) -> str:
        """
        Main function to simplify numbers in text.

        Args:
            raw_text (str): Input string containing text with numbers

        Returns:
            str: Text with numbers simplified according to rules
        """
        if not raw_text:
            return ""

        # First handle percentages
        text = re.sub(PERCENTAGE_PATTERN,
                      lambda m: self.get_descriptive_percentage(convert_german_number(m.group(1))),
                      raw_text)

        # Then handle regular numbers while preserving special cases
        number_pattern = fr'{NUMBER_PATTERN}(?:\s*(?:€|Euro|Kilogramm|kg))?'

        parts = []
        last_end = 0

        # Find all matches but process them only if they shouldn't be ignored
        for match in re.finditer(number_pattern, text):
            start, end = match.span()
            parts.append(text[last_end:start])
            parts.append(self.simplify_number(match, text))
            last_end = end

        parts.append(text[last_end:])

        return ''.join(parts)