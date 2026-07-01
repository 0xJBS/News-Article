import os
import re
import string
import zipfile
import xml.etree.ElementTree as ET

FILE_PATH = r"D:\Moringa\Module4\Assignments\News_Article\News Article for Python Assessment.docx"


# --------------------------------------------------
# READ DOCX FILE
# --------------------------------------------------
def read_docx_file(file_path):
    """Reads text from a DOCX file."""

    if not os.path.exists(file_path):
        return ""

    try:
        with zipfile.ZipFile(file_path) as docx:
            xml_content = docx.read("word/document.xml")

        root = ET.fromstring(xml_content)

        namespace = {
            "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
        }

        paragraphs = []

        for paragraph in root.findall(".//w:p", namespace):

            text = ""

            for run in paragraph.findall(".//w:t", namespace):

                if run.text:
                    text += run.text

            if text.strip():
                paragraphs.append(text.strip())

        return "\n\n".join(paragraphs)

    except Exception:
        return ""


# --------------------------------------------------
# COUNT SPECIFIC WORD
# --------------------------------------------------
def count_specific_word(text, search_word):
    """
    Counts how many times a word appears.

    Returns:
        int
    """

    if text == "" or search_word == "":
        return 0

    words = text.lower().split()

    count = 0

    for word in words:

        cleaned_word = word.strip(string.punctuation)

        if cleaned_word == search_word.lower():
            count += 1

    return count


# --------------------------------------------------
# IDENTIFY MOST COMMON WORD
# --------------------------------------------------
def identify_most_common_word(text):
    """
    Returns the most common word.

    Returns:
        str
    """

    if text.strip() == "":
        return None

    words = re.findall(r"\b\w+\b", text.lower())

    frequency = {}

    for word in words:

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    most_common = None
    highest = 0

    for word in frequency:

        if frequency[word] > highest:
            highest = frequency[word]
            most_common = word

    return most_common


# --------------------------------------------------
# CALCULATE AVERAGE WORD LENGTH
# --------------------------------------------------
def calculate_average_word_length(text):
    """
    Returns average word length.

    Returns:
        float
    """

    if text.strip() == "":
        return 0.0

    words = re.findall(r"\b\w+\b", text)

    if len(words) == 0:
        return 0.0

    total = 0

    for word in words:
        total += len(word)

    average = total / len(words)

    return float(average)


# --------------------------------------------------
# COUNT PARAGRAPHS
# --------------------------------------------------
def count_paragraphs(text):
    """
    Counts paragraphs separated by blank lines.

    Returns:
        int
    """

    if text.strip() == "":
        return 1

    paragraphs = text.split("\n\n")

    count = 0

    for paragraph in paragraphs:

        if paragraph.strip() != "":
            count += 1

    return count


# --------------------------------------------------
# COUNT SENTENCES
# --------------------------------------------------
def count_sentences(text):
    """
    Counts sentences using . ! ?

    Returns:
        int
    """

    if text.strip() == "":
        return 1

    count = 0

    index = 0

    while index < len(text):

        if text[index] == ".":
            count += 1

        elif text[index] == "!":
            count += 1

        elif text[index] == "?":
            count += 1

        index += 1

    return count


# --------------------------------------------------
# MAIN
# --------------------------------------------------
def main():

    print("=" * 45)
    print("      TEXT ANALYSIS REPORT GENERATOR")
    print("=" * 45)

    article = read_docx_file(FILE_PATH)

    if article == "":
        print("Unable to read the file.")
        return

    search_word = "Apple"

    print(f"\n1. Occurrence of '{search_word}': {count_specific_word(article, search_word)}")
    print(f"2. Most Common Word: {identify_most_common_word(article)}")
    print(f"3. Average Word Length: {calculate_average_word_length(article):.2f}")
    print(f"4. Total Number of Paragraphs: {count_paragraphs(article)}")
    print(f"5. Total Number of Sentences: {count_sentences(article)}")


if __name__ == "__main__":
    main()