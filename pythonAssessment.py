import os
import string
import zipfile
import xml.etree.ElementTree as ET


FILE_PATH = r"D:\Moringa\Module4\Assignments\News_Article\News Article for Python Assessment.docx"


def read_docx_file(file_path: str) -> str:
    """Extracts raw text from a DOCX file using built-in zip/xml parsers."""
    if not os.path.exists(file_path):
        return ""
    try:
        with zipfile.ZipFile(file_path) as docx_zip:
            xml_content = docx_zip.read('word/document.xml')
        root = ET.fromstring(xml_content)
        namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        
        paragraphs = []
        #   Loop"
        for paragraph in root.findall('.//w:p', namespaces):
            text_runs = [node.text for node in paragraph.findall('.//w:t', namespaces) if node.text]
            if text_runs:
                combined_text = "".join(text_runs).strip()
                if combined_text and not combined_text.startswith("[source:"):
                    paragraphs.append(combined_text)
                    
        return "\n\n".join(paragraphs)
    except Exception:
        return ""




def count_specific_word(text: str, search_word: str) -> int:
    """Counts occurrences of a word. Edge case: empty/no match returns 0."""
    # Conditional Value" (Explicit If/Else)
    if not text or not search_word:
        return 0
    else:
        # Lowercase and strip punctuation characters 
        cleaned_text = text.lower().translate(str.maketrans('', '', string.punctuation))
        words = cleaned_text.split()
        return words.count(search_word.lower())


def identify_most_common_word(text: str) -> str or None:
    """Identifies the most common word. Edge case: empty string returns None."""
    if not text.strip():
        return None
    else:
        cleaned_text = text.lower().translate(str.maketrans('', '', string.punctuation))
        words = cleaned_text.split()
        if not words:
            return None
        else:
            return max(set(words), key=words.count)


def calculate_average_word_length(text: str) -> float:
    """Calculates average word length as float, excluding punctuation. Empty returns 0.0."""
    if not text.strip():
        return 0.0
    else:
        cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
        words = cleaned_text.split()
        if not words:
            return 0.0
        else:
            total_chars = sum(len(word) for word in words)
            return float(total_chars / len(words))


def count_paragraphs(text: str) -> int:
    """Counts paragraphs based on empty lines. Edge case: empty string returns 1."""
    if not text.strip():
        return 1
    else:
        paragraphs = [p for p in text.split('\n\n') if p.strip()]
        return len(paragraphs)


def count_sentences(text: str) -> int:
    """Counts sentences using a while loop. Edge case: empty string returns 1."""
    if not text.strip():
        return 1
    else:
        sentence_endings = ('.', '!', '?')
        count = 0
        index = 0
        text_length = len(text)
        
        # While Loop
        while index < text_length:
            if text[index] in sentence_endings:
                count += 1
            index += 1
            
        if count > 0:
            return count
        else:
            return 1


def main():
    print("=========================================")
    print("      TEXT ANALYSIS REPORT GENERATOR     ")
    print("=========================================\n")
    
    # Extract file text
    article_text = read_docx_file(FILE_PATH)
    
    if not article_text:
        print(f"Error reading file at: {FILE_PATH}")
        return

    # 1. Count Specific Word
    search_term = "Apple"
    word_count = count_specific_word(article_text, search_term)
    print(f"1. Occurrence of the word '{search_term}': {word_count}")
    
    # 2. Identify Most Common Word
    common_word = identify_most_common_word(article_text)
    print(f"2. Most Common Word: '{common_word}'")
    
    # 3. Calculate Average Word Length
    avg_length = calculate_average_word_length(article_text)
    print(f"3. Average Word Length: {avg_length:.2f} characters")
    
    # 4. Count Paragraphs
    paragraph_count = count_paragraphs(article_text)
    print(f"4. Total Number of Paragraphs: {paragraph_count}")
    
    # 5. Count Sentences
    sentence_count = count_sentences(article_text)
    print(f"5. Total Number of Sentences: {sentence_count}")


if __name__ == "__main__":
    main()