
import re


class WordCountError(Exception):
    pass

def count_words(text: str) -> int:
    if not isinstance(text, str):
        raise WordCountError("Input must be a string")
    if len(text) == 0:
        return 0
    return len(re.split("[ -]",text))
    # split with hyphens
    # return len([word for word in text.replace("-", " ").split() if word.isalpha()])