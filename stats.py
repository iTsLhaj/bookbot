
def get_num_words(content: str) -> int:
    """
    accepts the text from the book as a string, and returns the number of words in the string
    """
    return content.split().__len__()

def get_char_occurence(content: str) -> dict[str, int]:
    """
    takes the text from the book as a string, and returns the number of times each character, (including symbols and spaces), appears in the string.
    """
    o = {}
    content = content.lower()
    charset = set(content)
    for c in charset:
        o[c] = content.count(c)
    return o
