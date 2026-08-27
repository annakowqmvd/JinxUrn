# test_jinxurn.py
"""
Tests for JinxUrn module.
"""

import unittest
from jinxurn import JinxUrn

class TestJinxUrn(unittest.TestCase):
    """Test cases for JinxUrn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = JinxUrn()
        self.assertIsInstance(instance, JinxUrn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = JinxUrn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
