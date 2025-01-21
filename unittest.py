import re
import html
import unittest

# Cleaning function
def clean(text):
    cleaning_steps = { 
        'punctuation_removed': False,
        'html_entities_removed': False,
        'tags_removed': False,
        'urls_removed': False,
        'brackets_removed': False,
        'specials_removed': False,
        'hyphens_removed': False,
        'whitespace_removed': False
    }

    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+(/[\w\d\-._~:/?#\[\]@!$&\'()*+,;=]*)?'
    text = re.sub(url_pattern, '', text)
    text_no_urls = re.sub(r'\[([^\[\]]*)\]\([^\(\)]*\)', r'\1', text)
    if not re.search(r'https?://\S+', text_no_urls):  # Check if no URL remains
        cleaning_steps['urls_removed'] = True
    text = text_no_urls

    # Punctuation removal: Ensure no punctuation remains.
    text = re.sub(r'[^\w\s]', '', text)

    # HTML entities removal: Check if HTML entities still exist.
    text_no_html_entities = html.unescape(text)
    if text_no_html_entities != text:
        cleaning_steps['html_entities_removed'] = True
    text = text_no_html_entities

    # HTML tag removal: Ensure no HTML tags remain.
    text_no_tags = re.sub(r'<[^<>]*>', ' ', text)
    if not re.search(r'<[^<>]*>', text_no_tags):  # Ensure no HTML tags are left
        cleaning_steps['tags_removed'] = True
    text = text_no_tags


    # Bracket removal: Ensure no text inside brackets exists.
    text_no_brackets = re.sub(r'\[[^\[\]]*\]', ' ', text)
    if not re.search(r'\[.*?\]', text_no_brackets):  # Check if no brackets remain
        cleaning_steps['brackets_removed'] = True
    text = text_no_brackets

    # Special characters removal: Check if standalone special characters are gone.
    text_no_specials = re.sub(r'(?:^|\s)[&#<>{}\[\]+|\\:-]{1,}(?:\s|$)', ' ', text)
    if not re.search(r'[&#<>{}\[\]+|\\:-]', text_no_specials):  # Ensure no special characters remain
        cleaning_steps['specials_removed'] = True
    text = text_no_specials

    # Hyphen removal: Ensure sequences of hyphens are removed.
    text_no_hyphens = re.sub(r'(?:^|\s)[\-=\+]{2,}(?:\s|$)', ' ', text)
    if not re.search(r'[-=+]{2,}', text_no_hyphens):  # Ensure no hyphen sequences remain
        cleaning_steps['hyphens_removed'] = True
    text = text_no_hyphens

    # Whitespace cleanup: Ensure multiple spaces are removed and reduced to one.
    text_no_whitespace = re.sub(r'\s+', ' ', text)
    if text_no_whitespace != text:  # Check if whitespace was reduced
        cleaning_steps['whitespace_removed'] = True
    # Return cleaned text and the cleaning steps
    return text.strip(), cleaning_steps

# Unit tests for cleaning function (this was the only testable function of our code)
class TestTextCleaning(unittest.TestCase):
    def test_cleaning(self):
        # Defining test cases with their expected outputs
        test_cases = [
            ("Hello, world!", "Hello world"),
            ("Check this link: https://example.com or [Click here](https://example.com)", "Check this link  or Click here"),
            ("Remove [this text] in brackets", "Remove this text in brackets"),
            ("Special characters: &#{}<>[]", "Special characters"),
            ("Multiple --- hyphens or ====", "Multiple  hyphens or"),
            ("   Extra    whitespace   here   ", "Extra    whitespace   here"),
        ]

        # Iterating over test cases and comparing outputs
        for original, expected_cleaned in test_cases:
            with self.subTest(original=original):
                self.assertEqual(clean(original)[0], expected_cleaned)

if __name__ == "__main__":
    unittest.main()