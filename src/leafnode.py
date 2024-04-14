from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self,
        value: str,  # noqa: E999
        tag: str | None = None,
        props: dict[str, str] | None = None,
    ) -> None:
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("Value property of lead node is required.")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
