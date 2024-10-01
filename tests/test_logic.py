import unittest
from utils.logic import calculate_speed, calculate_accuracy

class TestLogic(unittest.TestCase):
    """Unit tests for the logic functions."""

    def test_calculate_accuracy(self):
        """Test the calculate_accuracy function."""
        sample_text = "The quick brown fox"
        typed_text = "The quick brown"
        self.assertAlmostEqual(calculate_accuracy(sample_text, typed_text), 75.0)

        typed_text = "The quick brown fox"
        self.assertAlmostEqual(calculate_accuracy(sample_text, typed_text), 100.0)

        typed_text = "The quick"
        self.assertAlmostEqual(calculate_accuracy(sample_text, typed_text), 50.0)

    def test_calculate_speed(self):
        """Test the calculate_speed function."""
        typed_text = "The quick brown fox"
        time_taken = 30  # seconds
        self.assertAlmostEqual(calculate_speed(typed_text, time_taken), 8.0)

if __name__ == "__main__":
    unittest.main()