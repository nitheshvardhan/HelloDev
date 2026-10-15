import unittest
from main import greet

class TestGreeting(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(
            greet("Buddy"),
            "Hello, Buddy! Welcome to CI/CD."
        )

if __name__=="__main__":
    unittest.main()