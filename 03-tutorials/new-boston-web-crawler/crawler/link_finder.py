# serves as the basis for parsing text files formatted in HTML
from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    my_var = 55
    my_second_var = False

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            # attribute is the HTML-elements such as href, class, id, name, etc
            # value is the vaule of the attributes such as class='centered'
            for (attribute, value) in attrs:
                if attribute == 'href':
                    # adds relative url to the base url to get full url
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass
