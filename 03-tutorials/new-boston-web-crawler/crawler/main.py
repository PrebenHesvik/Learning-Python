import threading
from queue import Queue
from spider import Spider
from domain import get_domain_name
from general import (append_to_file, create_data_files, create_project_dir,
                     delete_file_contents, file_to_set, set_to_file,
                     write_file)


PROJECT_NAME = 'munck-cranes'
HOMEPAGE = 'http://munck-cranes.no/no'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
# thread queue
queue = Queue()
# create an instance of the Spider class for crawling the homepage
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        # make sure that the workers die when main exits
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        # call Spider.crawl page function
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        # add the links in the set to the thread queue
        queue.put(link)
    # make sure that the threads don't "bump" into each other
    queue.join()
    crawl()


# Check if there are items in the queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


# calling functions
create_workers()
crawl()
