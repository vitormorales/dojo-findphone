__author__ = 'vitor'

import unittest
from phone_converter import PhoneConverter


class ConversionTests(unittest.TestCase):
    def test_alphabet(self):
        self.assertEqual(PhoneConverter('ABCDEFGHIJKLMNOPQRSTUVWXYZ').convert(), '22233344455566677778889999')

    def test_sweet_home_alabama(self):
        self.assertEqual(PhoneConverter('SWEET-HOME-ALABAMA').convert(), '79338-4663-2522262')

    def test_sweet_home_alabama2(self):
        self.assertEqual(PhoneConverter().convert('SWEET-HOME-ALABAMA'), '79338-4663-2522262')

    def test_my_miserable_job(self):
        self.assertEqual(PhoneConverter().convert('MY-MISERABLE-JOB'), '69-647372253-562')

    def test_special_chars(self):
        self.assertEqual(PhoneConverter().convert('_*()[]'), '#ERROR#ERROR#ERROR#ERROR#ERROR#ERROR')


if __name__ == '__main__':
    unittest.main()