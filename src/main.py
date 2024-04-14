from textnode import TextNode


def main():
    t1 = TextNode("hey", "normal", None)
    t2 = TextNode("hey", "bold", "http://localhost:8888")
    t3 = TextNode("hey", "normal", None)
    print(f"t1 == t2: {t1 == t2}")
    print(f"t1 == t3: {t1 == t3}")
    print(t1)
    print(t2)
    print(t3)
    pass

main()
