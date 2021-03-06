import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from creditcard import formatter


class TestFormatter(unittest.TestCase):
    def test_visa_number(self):
        """should identify a visa card numbers."""
        visa_number = 4024007183310266
        self.assertTrue(formatter.is_visa(visa_number))

    def test_visa_number_string(self):
        """should identify a visa card number strings."""
        visa_string = '4024007183310266'
        self.assertTrue(formatter.is_visa(visa_string))

    def test_visa_electron_number(self):
        """should identify visa electron card numbers."""
        visa_electron_number = 4175004688713760
        self.assertTrue(formatter.is_visa_electron(visa_electron_number))

    def test_visa_electron_number_string(self):
        """should identify visa electron card number strings."""
        visa_electron_string = '4175004688713760'
        self.assertTrue(formatter.is_visa_electron(visa_electron_string))

    def test_mastercard_number(self):
        """should identify mastercard card numbers."""
        mastercard_number = 5409219472999830
        self.assertTrue(formatter.is_mastercard(mastercard_number))

    def test_mastercard_number_string(self):
        """should identify mastercard card number strings."""
        mastercard_string = '5409219472999830'
        self.assertTrue(formatter.is_mastercard(mastercard_string))

    def test_amex_number(self):
        """should identify american express card numbers."""
        amex_number = 374619657687666
        self.assertTrue(formatter.is_amex(amex_number))

    def test_amex_number_string(self):
        """should identify american express card number strings."""
        amex_string = '374619657687666'
        self.assertTrue(formatter.is_amex(amex_string))

    def test_maestro_number(self):
        """should identify maestro card numbers."""
        maestro_number = 6304236404755563
        self.assertTrue(formatter.is_maestro(maestro_number))

    def test_maestro_number_string(self):
        """should identify maestro card number strings."""
        maestro_string = '6304236404755563'
        self.assertTrue(formatter.is_maestro(maestro_string))

    def test_discover_number(self):
        """should identify discovery card numbers."""
        discover_number = 6011359876556543
        self.assertTrue(formatter.is_discover(discover_number))

    def test_discover_number_string(self):
        """should identify discovery card number strings."""
        discover_string = '6011359876556543'
        self.assertTrue(formatter.is_discover(discover_string))

    def test_unknown_formats(self):
        """should return none for unknown card formats."""
        unknown = 1234567890
        self.assertEqual(formatter.get_format(unknown), [])

    def test_single_format_of_number(self):
        """should get the format of a card number."""
        number = 5409219472999830
        self.assertEqual(formatter.get_format(number), ['mastercard'])

    def test_dual_formats_of_number(self):
        """should get multiple formats of a card number."""
        number = 4508077077058854
        self.assertEqual(formatter.get_format(number), ['visa', 'visa electron'])
