from unittest import TestCase

import namegen

class TestFirstName(TestCase):
    def test_is_string(self):
        s = namegen.getname(1972, 'M')
        self.assertTrue(isinstance(s, basestring))
    def test_lower_bound(self):
        s = namegen.getname(1805, 'F')
        self.assertEqual(s, '')
