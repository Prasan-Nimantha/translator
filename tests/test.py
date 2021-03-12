import unittest
from translator import english_to_french, english_to_german


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        with self.assertRaises(Exception):
            english_to_french("")
    
    def test2(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test3(self):
        self.assertEqual(english_to_french("My name"), "Mon nom")

    def test4(self):
        self.assertNotEqual(english_to_french("hello world"), "hello world")


class TestEnglishToGerman(unittest.TestCase):
    def test1(self):
        with self.assertRaises(Exception):
            english_to_german("")

    def test2(self):
        self.assertEqual(english_to_german("Hello"), "Hallo")

    def test3(self):
        self.assertEqual(english_to_german("How are you"), "Wie geht es Ihnen?")
        
    def test4(self):
        self.assertNotEqual(english_to_german("hello world"), "hello world")


unittest.main()
