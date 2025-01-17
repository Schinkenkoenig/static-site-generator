class HTMLNode:
    def __init__(
        self,
        children: list["HTMLNode"] | None = None,
        value: str | None = None,
        tag: str | None = None,
        props: dict[str, str] | None = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        pass

    def to_html(self) -> str:
        raise NotImplementedError()

    def props_to_html(self) -> str:
        if self.props is None or not self.props:
            return ""
        return "".join([f' {k}="{v}"' for k, v in self.props.items()])

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"
