import unittest
from Assignment4.loop import calculate_bmi, determine_bmi_category 


class TestBMICalculator(unittest.TestCase):
    
    def test_valid_bmi_normal(self):
        """Test BMI calculation for a normal weight case."""
        bmi = calculate_bmi(150, 5, 8)
        self.assertAlmostEqual(bmi, 22.8, places=1)
        self.assertEqual(determine_bmi_category(bmi), "Normal weight")
    
    def test_valid_bmi_underweight(self):
        """Test BMI calculation for an underweight case."""
        bmi = calculate_bmi(100, 5, 7)
        self.assertAlmostEqual(bmi, 15.7, places=1)
        self.assertEqual(determine_bmi_category(bmi), "Underweight")
    
    def test_invalid_zero_height(self):
        """Test that a zero height raises a ValueError."""
        with self.assertRaises(ValueError):
            calculate_bmi(150, 0, 0)
    
    def test_invalid_negative_weight(self):
        """Test that a negative weight raises a ValueError."""
        with self.assertRaises(ValueError):
            calculate_bmi(-150, 5, 8)
    
    def test_valid_bmi_obesity(self):
        """Test BMI calculation for an obesity case."""
        bmi = calculate_bmi(250, 5, 4)
        self.assertAlmostEqual(bmi, 42.9, places=1)
        self.assertEqual(determine_bmi_category(bmi), "Obesity")

if __name__ == "__main__":
    unittest.main()
