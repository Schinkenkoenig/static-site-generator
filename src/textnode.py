from typing import Callable
from leafnode import LeafNode


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


def delimiter_to_text_type(delimiter: str) -> str:
    map = {"**": text_type_bold, "*": text_type_italic, "`": text_type_code}
    if delimiter not in map.keys():
        raise ValueError(f"Unknown delimiter {delimiter}.")
    return map[delimiter]


class TextNode:
    def __init__(self, text: str, text_type: str, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, TextNode):
            return False
        return (
            self.text == value.text
            and self.text_type == value.text_type
            and self.url == value.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node: TextNode):
    map: dict[str, Callable[[TextNode], LeafNode]] = {
        text_type_text: lambda t: LeafNode(value=t.text),
        text_type_bold: lambda t: LeafNode(tag="b", value=t.text),
        text_type_italic: lambda t: LeafNode(tag="i", value=t.text),
        text_type_code: lambda t: LeafNode(tag="code", value=t.text),
        text_type_link: lambda t: LeafNode(
            tag="a", value=t.text, props={"href": t.url or ""}
        ),
        text_type_image: lambda t: LeafNode(
            tag="img", value="", props={"src": t.url or "", "alt": t.text}
        ),
    }
    if text_node.text_type not in map:
        raise ValueError(f"Text type {text_node.text_type} is not supported.")
    return map[text_node.text_type](text_node)


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: str
) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            new_nodes.append(node)
            continue
        splitted_text = node.text.split(delimiter)
        if len(splitted_text) == 1:
            new_nodes.append(node)
            continue
        if len(splitted_text) % 2 == 0:
            raise ValueError(
                f"Node with text {node.text} is unbalance for delimiter {delimiter}."
            )

        for i, text in enumerate(splitted_text):
            if i % 2 == 0 and text:
                node = TextNode(text, text_type_text)
                new_nodes.append(node)
                continue

            node = TextNode(text, text_type)
            new_nodes.append(node)
    return new_nodes
