
from src.number_simplifier.simplifier import NumberSimplifier


class TextSimplifierApp:
    def __init__(self):
        self.simplifier = NumberSimplifier()

    def process_single_text(self, text: str) -> None:
        """Process a single text input and display result."""
        result = self.simplifier.simplify_numbers(text)
        print("\nInput:  ", text)
        print("Output: ", result)

    def run_test_cases(self) -> None:
        """Run predefined test cases."""
        test_cases = [
            "324.620,22 Euro wurden gespendet.",
            "1.897 Menschen nahmen teil.",
            "25 Prozent der Bevölkerung sind betroffen.",
            "90 Prozent stimmten zu.",
            "14 Prozent lehnten ab.",
            "Bei 38,7 Grad Celsius ist es sehr heiß.",
            "denn die Rente steigt um 4,57 Prozent.",
            "1.000.000 Euro wurden gespendet.",
            "10.000 Menschen waren anwesend.",
            "250 Kilogramm wiegt die Lieferung.",
            "30 Prozent der Fläche sind betroffen.",
            "Die Temperatur beträgt -15,5 Grad.",
            "Am 1. Januar 2024 waren es 5.678 Teilnehmer.",
            "1.234.567,89€ wurden überwiesen.",
            "60 Prozent der Teilnehmer stimmten zu.",
            "Der Anteil beträgt 33 Prozent der Gesamtfläche.",
            "Im Jahr 2024 gab es 1.234 Ereignisse.",
            "Der pH-Wert beträgt 7,4.",
            "Um 15:30 Uhr beginnt der Termin."
        ]

        print("Running test cases...")
        for test in test_cases:
            self.process_single_text(test)

    def interactive_mode(self) -> None:
        """Run in interactive mode where user can input text."""
        print("\nInteractive Mode - Enter text to simplify (or 'q' to quit)")
        while True:
            text = input("\nEnter text: ")
            if text.lower() == 'q':
                break
            self.process_single_text(text)


def main():
    app = TextSimplifierApp()

    while True:
        print("\nNumber Simplifier")
        print("1. Run test cases")
        print("2. Interactive mode")
        print("3. Exit")

        choice = input("\nSelect an option (1-3): ")

        if choice == "1":
            app.run_test_cases()
        elif choice == "2":
            app.interactive_mode()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()