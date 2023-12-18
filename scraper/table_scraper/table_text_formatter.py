import re

REGEX_REFERENCE = r"\[[^\]]*\]"
SPLIT_WORDS_REGEX = r"\s+|(?<=\w)(?=[A-Z])"


def format_cell_text(cell_text):
    if not cell_text:
        return ""
    cell_text = remove_reference(cell_text)
    cell_text = remove_duplicates(cell_text)
    return cell_text


def remove_reference(cell_text):
    if cell_text:
        text = re.sub(REGEX_REFERENCE, "", cell_text)
        return text.strip()
    return ""


def remove_duplicates(text):
    words = re.split(SPLIT_WORDS_REGEX, text)
    unique_words = []

    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    return " ".join(unique_words)
