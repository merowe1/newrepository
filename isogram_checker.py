import unittest

def is_isogram(word):
    word = word.lower()
    unique_letters = set(word)
    return len(word) == len(unique_letters)

class TestIsIsogram(unittest.TestCase):
    def test_isogram_word(self):
        # Test a valid isogram word
        self.assertTrue(is_isogram("isogram"))

    

if __name__ == '__main__':
    unittest.main()
