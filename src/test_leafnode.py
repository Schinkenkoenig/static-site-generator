import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_html_str(self):
        expected = "<p>This is a paragraph of text.</p>"
        expected2 = '<a href="https://www.google.com">Click me!</a>'

        node = LeafNode(tag="p", value="This is a paragraph of text.")
        node2 = LeafNode(
            tag="a", value="Click me!", props={"href": "https://www.google.com"}
        )

        html = node.to_html()
        html2 = node2.to_html()

        self.assertEqual(expected, html)
        self.assertEqual(expected2, html2)

    def test_just_str_to_html(self):
        expected = "hey there"

        node = LeafNode(value=expected)
        html = node.to_html()
        self.assertEqual(expected, html)

    def test_leaf_requires_value(self):
        node = LeafNode(value=None)
        self.assertRaises(ValueError, lambda: node.to_html())
