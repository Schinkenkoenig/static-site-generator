import unittest

from textnode import (
    TextNode,
    split_nodes_delimiter,
    text_node_to_html_node,
    text_type_code,
    text_type_text,
    text_type_bold,
    text_type_image,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_text_to_html_bold(self):
        node = TextNode(text="I am bold", text_type=text_type_bold)
        expected = "<b>I am bold</b>"

        html_node = text_node_to_html_node(node)
        html = html_node.to_html()

        self.assertEqual(expected, html)

    def test_text_to_html_img(self):
        node = TextNode(
            text="I am an image",
            text_type=text_type_image,
            url="http://www.google.de/logo.png",
        )
        expected = '<img src="http://www.google.de/logo.png" alt="I am an image"></img>'

        html_node = text_node_to_html_node(node)
        html = html_node.to_html()

        self.assertEqual(expected, html)

    def test_split_delimiter_raise_unbalanced(self):
        text = "I am `cool yeah"
        node = TextNode(text, text_type_text)

        def act():
            return split_nodes_delimiter([node], "`", text_type_code)

        self.assertRaises(ValueError, act)

    def test_split_delimiter_no_delim_in_text(self):
        text = "I am cool yeah"
        node = TextNode(text, text_type_text)

        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(len(new_nodes), 1)
        single_node = new_nodes[0]
        self.assertEqual(single_node.text, text)
        self.assertEqual(single_node.text_type, text_type_text)

    def test_split_delimiter_simple_case(self):
        text = "I `am` cool"
        node = TextNode(text, text_type_text)

        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(len(new_nodes), 3)
        node = new_nodes[0]
        node_code = new_nodes[1]
        node2 = new_nodes[2]

        self.assertEqual(node_code.text, "am")
        self.assertEqual(node_code.text_type, text_type_code)

        self.assertEqual(node.text, "I ")
        self.assertEqual(node.text_type, text_type_text)
        self.assertEqual(node2.text, " cool")
        self.assertEqual(node2.text_type, text_type_text)
        pass
