def word_count(text: str) -> int:
    return len(text.split())


def slugify(text: str) -> str:
    return "-".join(text.lower().split())
