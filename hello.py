# See: https://docs.python.org/3/library/unittest.html


import unittest


def has_trailing_whitespace(line):
    return line.rstrip() != line


def has_tab_indentation(line):
    return '\t' in get_leading_whitespace(line)


def get_leading_whitespace(line):
    return line[0:len(line) - len(line.lstrip())]


def has_wrong_spaces_count(line):
    return len(get_leading_whitespace(line)) % 4 != 0


def has_empty_first_line(line):
    pass
# check line endings

# def has_leading_whitespace(line):
#     return len(line) - len(line.lstrip()) > 0


class TestStringMethods(unittest.TestCase):
    def test_trailing_whitespace(self):
        self.assertTrue(has_trailing_whitespace(' '))
        self.assertTrue(has_trailing_whitespace('    '))
        self.assertTrue(has_trailing_whitespace('\t'))
        self.assertTrue(has_trailing_whitespace('a = 1 '))

        self.assertFalse(has_trailing_whitespace(''))
        self.assertFalse(has_trailing_whitespace('a = 1'))

    def test_get_leading_whitespace(self):
        self.assertEqual(get_leading_whitespace('    a = 1'), '    ')
        self.assertEqual(get_leading_whitespace('\ta = 1'), '\t')

    def test_has_tab_indentation(self):
        self.assertTrue(has_tab_indentation('\ta = 1'))
        self.assertTrue(has_tab_indentation('\t\ta = 1'))

        self.assertFalse(has_tab_indentation('a = 1'))
        self.assertFalse(has_tab_indentation('    a = 1'))
        self.assertFalse(has_tab_indentation('        a = 1'))

    def test_has_wrong_spaces_count(self):
        self.assertTrue(has_wrong_spaces_count(' a = 1'))
        self.assertTrue(has_wrong_spaces_count('  a = 1'))
        self.assertTrue(has_wrong_spaces_count('   a = 1'))

        self.assertFalse(has_wrong_spaces_count('    a = 1'))

    # def test_has_leading_whitespace(self):
    #     self.assertTrue(has_leading_whitespace('    a = 1'))

    #     self.assertFalse(has_leading_whitespace('a = 1'))
    """def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.spplit fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)"""


if __name__ == '__main__':
    unittest.main()
