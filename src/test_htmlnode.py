import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_str(self):
        expected = ' href="https://www.google.com" target="_blank"'
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})

        props_str = node.props_to_html()
        self.assertEqual(expected, props_str)

    def test_simple_repr(self):
        expected = 'HTMLNode(a, None, [HTMLNode(span, Google, None,  class="yomomma" id="mommy")],  href="https://www.google.com" target="_blank")'

        child = HTMLNode(
            tag="span", value="Google", props={"class": "yomomma", "id": "mommy"}
        )
        node = HTMLNode(
            tag="a",
            children=[child],
            props={"href": "https://www.google.com", "target": "_blank"},
        )

        self.assertEqual(expected, str(node))
