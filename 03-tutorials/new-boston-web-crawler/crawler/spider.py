from urllib.request import urlopen
from link_finder import LinkFinder
# from domain import *
from general import (append_to_file, create_data_files, create_project_dir,
                     delete_file_contents, file_to_set, set_to_file,
                     write_file)


class Spider:

    # class variables - shared among all instances
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    # Creates directory and files for project on first run and starts the spider
    @staticmethod
    def boot():
        # create project directory
        create_project_dir(Spider.project_name)
        # Create queue and crawled files
        create_data_files(Spider.project_name, Spider.base_url)
        # open up queue text file, and append all urls to set
        Spider.queue = file_to_set(Spider.queue_file)
        # open up crawled text file, and append all urls to set
        Spider.crawled = file_to_set(Spider.crawled_file)

    # Updates user display, fills queue and updates files
    @staticmethod
    def crawl_page(thread_name, page_url):
        # check that the page has not been crawled
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled  ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            # runs set_to_file function
            Spider.update_files()

    # Converts raw response data into readable information and checks for proper html formatting
    # returns a set of urls/links
    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            # make sure we are only reading text, and not an executable
            if 'text/html' in response.getheader('Content-Type'):
                # The page content is read as bytes
                html_bytes = response.read()
                # converts bytes into string format
                html_string = html_bytes.decode("utf-8")
            # create instance of class
            finder = LinkFinder(Spider.base_url, page_url)
            # takes an entire HTML document and returns ONLY the tags of that document
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        # finder.page_links return the set of urls
        return finder.page_links()

    # Saves queue data to project files
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            # if url is not connected to website we are trying to crawl
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
