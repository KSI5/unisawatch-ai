from bs4 import BeautifulSoup


def extract_text(html):
    """
    Extract readable text from HTML.
    """
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator=" ", strip=True)


def contains_keyword(text, keywords):
    """
    Check if any keyword exists in the page text.
    """
    text = text.lower()

    for keyword in keywords:
        if keyword.lower() in text:
            return keyword

    return None