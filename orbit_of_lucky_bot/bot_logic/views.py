from requests import get

from .utils.parser import parser_html_all, parser_html_get
from .conf import HEADERS, CHIP_URL_BASE


def arduino_sections_list_view(base_url: str) -> list:
    """Выведет список ссылок разделов arduino"""
    
    response = get(url=f'{base_url}/manufacturer/arduino', headers=HEADERS)

    if response:
        if 'text/html' in response.headers.get('Content-Type', ''):
            data = parser_html_all(
                resp_text=response.text, 
                block_html='a',
                class_html=None
            )
            data_links = [
                f'<a href="{base_url}{href}">'
                f'{href.split("/")[-1].split("?")[0]}</a>\n' 
                for data_bs4 in data 
                if (href := data_bs4.get('href'))
            ]
            list_links = ['<strong>arduino sections</strong>\n\n'] + \
                list(set(filter(
                    lambda line: 'catalog-show' in line, data_links
                )))

            return list_links
        return None
    return None


def arduino_section_get_view(base_url: str, section: str) -> str:
    """Выведет ссылку на раздел arduino"""

    list_links = arduino_sections_list_view(base_url=base_url)
    not_found = f'<b>На сайте нет разделов с содержанием: {section}!</b>'

    if list_links:
        for link in list_links:
            if section in link:
                url = link.split('"')[1]
                name = url.split('/')[-1].split('?')[0]
                link = {f'name': name, 'url': url}
                return link
        return not_found
    return not_found


if __name__ == '__main__':
    test_get_arduino_sections = arduino_sections_list_view(
        base_url=CHIP_URL_BASE
    )
    print(test_get_arduino_sections)
    
    # test_get_arduino_section = arduino_section_get_view(
    #     base_url=CHIP_URL_BASE,
    #     section='sensors'
    # )
    # print(test_get_arduino_section)
