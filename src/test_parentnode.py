import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_html_str(self):
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        parent = ParentNode(
            tag="p",
            children=[
                LeafNode(tag="b", value="Bold text"),
                LeafNode(tag=None, value="Normal text"),
                LeafNode(tag="i", value="italic text"),
                LeafNode(tag=None, value="Normal text"),
            ],
        )

        html = parent.to_html()

        self.assertEqual(expected, html)
