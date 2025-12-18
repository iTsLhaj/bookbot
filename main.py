import io
import sys

try:
    fp = sys.argv[1]
except Exception:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)

from stats import (
    get_num_words,
    get_char_occurence
    )



def get_book_text(filePath: str) -> str:
    """
    It takes a filepath as input and returns the contents of the file as a string.
    """
    try:
        with io.open(file=filePath, mode='r') as fs:
            return fs.read()
    except Exception:
        return ""

def pretty_report(filePath: str, content: str, wc: int, occ: dict[str, int]) -> None:
    report = f"""============ BOOKBOT ============
Analyzing book found at {filePath}
----------- Word Count ----------
Found {wc} total words
--------- Character Count -------
{"\n".join([f"{i['char']}: {i['count']}" for i in sorted([{"char": k, "count": v} for k, v in get_char_occurence(content).items()], reverse=True, key=lambda i: i["count"])])}
============= END ===============
"""
    print(report)

def main():
    # bookPath = 'books/frankenstein.txt'
    content = get_book_text(fp)

    pretty_report(
        fp, content, get_num_words(content),
        get_char_occurence(content)
        )

main()

