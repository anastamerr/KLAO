
import unittest
from src.number_simplifier.number_simplifier import NumberSimplifier

class TestNumberSimplifier(unittest.TestCase):
    def setUp(self):
        self.simplifier = NumberSimplifier()

    def test_basic_numbers(self):
        test_cases = [
            ("324.620,22 Euro wurden gespendet.",
             "etwa 325.000 Euro wurden gespendet."),
            ("1.897 Menschen nahmen teil.",
             "etwa 2.000 Menschen nahmen teil."),
            ("Bei 38,7 Grad Celsius ist es sehr heiß.",
             "Bei etwa 39 Grad Celsius ist es sehr heiß."),
        ]
        for input_text, expected in test_cases:
            self.assertEqual(self.simplifier.simplify_numbers(input_text), expected)

    def test_percentages(self):
        test_cases = [
            ("25 Prozent der Bevölkerung sind betroffen.",
             "jeder Vierte der Bevölkerung sind betroffen."),
            ("90 Prozent stimmten zu.",
             "fast alle stimmten zu."),
            ("14 Prozent lehnten ab.",
             "wenige lehnten ab."),
        ]
        for input_text, expected in test_cases:
            self.assertEqual(self.simplifier.simplify_numbers(input_text), expected)

    def test_large_numbers(self):
        test_cases = [
            ("1.000.000 Euro wurden gespendet.",
             "etwa 1,0 Million Euro (So viel Geld, dass man 100 Autos kaufen könnte) wurden gespendet."),
            ("10.000 Menschen waren anwesend.",
             "etwa 10.000 Menschen (So viele Menschen, wie in ein großes Fußballstadion passen) waren anwesend."),
        ]
        for input_text, expected in test_cases:
            self.assertEqual(self.simplifier.simplify_numbers(input_text), expected)

    def test_special_cases(self):
        test_cases = [
            ("Der pH-Wert beträgt 7,4.",
             "Der pH-Wert beträgt 7,4."),
            ("Um 15:30 Uhr beginnt der Termin.",
             "Um 15:30 Uhr beginnt der Termin."),
            ("Am 1. Januar 2024 waren es 5.678 Teilnehmer.",
             "Am 1. Januar 2024 waren es 5.678 Teilnehmer."),
        ]
        for input_text, expected in test_cases:
            self.assertEqual(self.simplifier.simplify_numbers(input_text), expected)

if __name__ == '__main__':
    unittest.main()