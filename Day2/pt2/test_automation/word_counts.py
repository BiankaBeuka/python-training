
class WordCountError(Exception):
    pass

def count_words(text: str) -> int:
    if not isinstance(text, str):
        raise WordCountError("Input must be a string")
    return len([word for word in text.split() if word.isalpha()])
