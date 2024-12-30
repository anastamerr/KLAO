
def convert_german_number(number_str: str) -> str:
    """Convert German number format to standard format."""
    return number_str.replace('.', '').replace(',', '.')

def format_number(number: float, decimals: int = 1) -> str:
    """Format number with German decimal separator."""
    return format(number, f'.{decimals}f').replace('.', ',')