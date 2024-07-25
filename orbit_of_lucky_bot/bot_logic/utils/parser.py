from bs4 import BeautifulSoup as Soup


def parser_html_all(
        resp_text: str, 
        block_html: str, 
        class_html: str=None
    ) -> Soup:
    """Получает объкт soup из html по class и блоку (list)"""

    soup = Soup(resp_text, 'html.parser')
    
    if class_html:
        data = soup.find_all(block_html, class_=class_html)
    else:
        data = soup.find_all(block_html)

    if data:
        return data
    return None


def parser_html_get(
        resp_text: str, 
        block_html: str, 
        class_html: str=None
    ) -> Soup:
    """Получает объкт soup из html по class и блоку (get)"""

    soup = Soup(resp_text, 'html.parser')

    if class_html:
        data = soup.find(block_html, class_=class_html)
    else:
        data = soup.find(block_html)

    if data:
        return data
    return None
