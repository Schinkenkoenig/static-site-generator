from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self,
        children: list["HTMLNode"],
        tag: str | None = None,
        props: dict[str, str] | None = None,
    ) -> None:
        super().__init__(children=children, tag=tag, props=props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("Tag is required for a parent node")

        if not self.children:
            raise ValueError("A parent node needs to have children.")

        children_html = "".join([c.to_html() for c in self.children])

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
