import unittest
from converters import Converters

class TestCases(unittest.TestCase):
  def setUp(self):
    pass

  def test_single_style(self):
    html = "<div style='background-color: blue;'></div>"
    expected_html = '<div class="newClass1">\n</div>'
    expected_css = '.newClass1 {\n\tbackground-color:blue,\n}\n\n'

    cssClasses, newHtml = Converters().convertStyleToClass(html)

    self.assertEqual(newHtml, expected_html)
    self.assertEqual(cssClasses, expected_css)

  def test_multiple_styles(self):
    html = "<div style='background-color: blue; text-align: center;'></div>"
    expected_html = '<div class="newClass1">\n</div>'
    expected_css = '.newClass1 {\n\tbackground-color:blue,\n\ttext-align:center,\n}\n\n'

    cssClasses, newHtml = Converters().convertStyleToClass(html)

    self.assertEqual(newHtml, expected_html)
    self.assertEqual(cssClasses, expected_css)

  def test_multiple_classes(self):
    html = "<div style='background-color: blue;'><div style='text-align: center;'></div></div>"
    expected_html = '<div class="newClass1">\n <div class="newClass2">\n </div>\n</div>'
    expected_css = '.newClass1 {\n\tbackground-color:blue,\n}\n\n.newClass2 {\n\ttext-align:center,\n}\n\n'

    cssClasses, newHtml = Converters().convertStyleToClass(html)

    self.assertEqual(newHtml, expected_html)
    self.assertEqual(cssClasses, expected_css)

  def test_duplicate_ordered_classes(self):
    html = "<div style='background-color: blue; text-align: center;'><div style='background-color: blue; text-align: center;'></div></div>"
    expected_html = '<div class="newClass1">\n <div class="newClass1">\n </div>\n</div>'
    expected_css = '.newClass1 {\n\tbackground-color:blue,\n\ttext-align:center,\n}\n\n'

    cssClasses, newHtml = Converters().convertStyleToClass(html)

    self.assertEqual(newHtml, expected_html)
    self.assertEqual(cssClasses, expected_css)

  def test_duplicate_unordered_classes(self):
    html = "<div style='text-align: center; background-color: blue;'><div style='background-color: blue; text-align: center;'></div></div>"
    expected_html = '<div class="newClass1">\n <div class="newClass1">\n </div>\n</div>'
    expected_css = '.newClass1 {\n\tbackground-color:blue,\n\ttext-align:center,\n}\n\n'

    cssClasses, newHtml = Converters().convertStyleToClass(html)

    self.assertEqual(newHtml, expected_html)
    self.assertEqual(cssClasses, expected_css)


if __name__ == '__main__':
    unittest.main()
