# test_cryptokey.py
"""
Tests for CryptoKey module.
"""

import unittest
from cryptokey import CryptoKey

class TestCryptoKey(unittest.TestCase):
    """Test cases for CryptoKey class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoKey()
        self.assertIsInstance(instance, CryptoKey)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoKey()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
